# Module information:
# - This folder contains the Python source codes used for training, testing Machine Learning model and then use it for makeing predictions.
# File: __init__.py
# Functionality: Making ```models``` become a Python module
from typing import Iterator
import torch
import torch.nn as nn
from torch.nn import functional as F
from d2l import torch as d2l
import matplotlib.pyplot as plt

class Module(nn.Module, d2l.HyperParameters):  #@save
    """The base class of models."""
    def __init__(self, plot_train_per_epoch=2, plot_valid_per_epoch=1):
        super().__init__()
        self.save_hyperparameters()
        self.board = d2l.ProgressBoard()

    def loss(self, y_hat, y):
        raise NotImplementedError

    def forward(self, X):
        if not hasattr(self, 'net'):
            raise AttributeError('Neural network is not defined')
        return self.net(X)

    def plot(self, key, value, train):
        """Plot a point in animation."""
        if not hasattr(self, 'trainer'):
            raise AttributeError('Trainer is not initialized')
        self.board.xlabel = 'epoch'
        x, n = self._get_plot_params(train)
        self.board.draw(x, value.to(d2l.cpu()).detach().numpy(),
                        ('train_' if train else 'val_') + key,
                        every_n=int(n))

    def _get_plot_params(self, train):
        if train:
            return self.trainer.train_batch_idx / self.trainer.num_train_batches, self.trainer.num_train_batches / self.plot_train_per_epoch
        else:
            return self.trainer.epoch + 1, self.trainer.num_val_batches / self.plot_valid_per_epoch

    def training_step(self, batch):
        l = self.loss(self(*batch[:-1]), batch[-1])
        self.plot('loss', l, train=True)
        return l

    def validation_step(self, batch):
        l = self.loss(self(*batch[:-1]), batch[-1])
        self.plot('loss', l, train=False)

    def configure_optimizers(self):
        raise NotImplementedError
    
class Trainer(d2l.HyperParameters):  #@save
    """The base class for training models with data."""
    def __init__(self, max_epochs, num_gpus=0, gradient_clip_val=0):
        self.save_hyperparameters()
        assert num_gpus == 0, 'No GPU support yet'

    def prepare_data(self, data):
        self.train_dataloader = data.get_dataloader(train=True)
        self.val_dataloader = data.get_dataloader(train=False)
        self._set_num_batches()

    def _set_num_batches(self):
        self.num_train_batches = len(self.train_dataloader)
        self.num_val_batches = len(self.val_dataloader) if self.val_dataloader is not None else 0

    def prepare_model(self, model):
        model.trainer = self
        model.board.xlim = [0, self.max_epochs]
        self.model = model

    def fit(self, model, data):
        self.prepare_data(data)
        self.prepare_model(model)
        self._initialize_training_state()
        for self.epoch in range(self.max_epochs):
            self.fit_epoch()

    def _initialize_training_state(self):
        self.optim = self.model.configure_optimizers()
        self.epoch = 0
        self.train_batch_idx = 0
        self.val_batch_idx = 0

    def fit_epoch(self):
        raise NotImplementedError


class SGD(d2l.HyperParameters):  #@save
    def __init__(self, params, lr):
        self.params = params
        self.lr = lr
        self.save_hyperparameters()
        
    def step(self):
        with torch.no_grad():
            for param in self.params:
                param -= self.lr * param.grad
                param.grad.zero_()
    
    def zero_grad(self):
        for param in self.params:
            if param.grad is not None:
                param.grad.data.zero_()

# Linear Regression

class LinearRegressionFromScratch(Module):
    def __init__(self, num_inputs, lr, sigma=0.01, plot_train_per_epoch=2, plot_valid_per_epoch=1):
        super().__init__(plot_train_per_epoch, plot_valid_per_epoch)
        self.w = torch.normal(0, sigma, size=(num_inputs, 1), requires_grad=True)
        self.b = torch.zeros(1, requires_grad=True)
        self.lr=lr

    def loss(self, y_hat, y):
        l = (y_hat - y.reshape(y_hat.shape))**2 / 2
        return l.mean()

    def forward(self, X):
        return torch.matmul(X, self.w) + self.b
    
    def configure_optimizers(self):
        return SGD([self.w, self.b], self.lr)

class LinearRegressionTrainer(Trainer):
    def __init__(self, max_epochs, num_gpus=0, gradient_clip_val=0):
        super().__init__(max_epochs, num_gpus, gradient_clip_val)
    
    def prepare_batch(self, batch):
        return batch
    
    def fit_epoch(self):
        # Training
        self.model.train()
        for batch in self.train_dataloader:
            loss = self.model.training_step(self.prepare_batch(batch))
            self.optim.zero_grad()
            with torch.no_grad():
                loss.backward()
                if self.gradient_clip_val > 0:  # To be discussed later
                    self.clip_gradients(self.gradient_clip_val, self.model)
                self.optim.step()
            self.train_batch_idx += 1
        # Validation
        if self.val_dataloader is None:
            return
        self.model.eval()
        for batch in self.val_dataloader:
            with torch.no_grad():
                self.model.validation_step(self.prepare_batch(batch))
            self.val_batch_idx += 1

class LinearRegression(Module):
    def __init__(self, lr):
        super().__init__()
        self.save_hyperparameters()
        self.net = nn.LazyLinear(1)
        self.net.weight.data.normal_(0, 0.01)
        self.net.bias.data.fill_(0)
        
    def loss(self, y_hat, y):
        fn = nn.MSELoss()
        return fn(y_hat, y.reshape(y_hat.shape))
    
    def forward(self, X):
        return self.net(X)
    
    def configure_optimizers(self):
        return torch.optim.SGD(self.parameters(), lr=self.lr)
    
    def get_wb(self):
        return self.net.weight.data, self.net.bias.data
    
# Softmax Regression
class Classifier(Module):  #@save
    """The base class of classification models."""
    def validation_step(self, batch):
        Y_hat = self(*batch[:-1])
        self.plot('loss', self.loss(Y_hat, batch[-1]), train=False)
        self.plot('acc', self.accuracy(Y_hat, batch[-1]), train=False)
    
    def accuracy(self, Y_hat, Y, averaged=True):
        Y_hat = Y_hat.reshape((-1, Y_hat.shape[-1]))
        preds = Y_hat.argmax(axis=1).type(Y.dtype)
        compare = (preds == Y.reshape(-1)).type(torch.float32)
        return compare.mean() if averaged else compare
    
    def configure_optimizers(self):
        return torch.optim.SGD(self.parameters(), lr=self.lr)

def softmax(X):
    X_exp = torch.exp(X)
    partition = X_exp.sum(1, keepdim=True)
    return X_exp / partition  # The broadcasting mechanism is applied here

def cross_entropy(y_hat, y):
    return - torch.log(y_hat[range(len(y_hat)), y])

class SoftmaxRegression(d2l.Classifier):  #@save
    """The softmax regression model."""
    def __init__(self, num_outputs, lr):
        super().__init__()
        self.save_hyperparameters()
        self.net = nn.Sequential(nn.Flatten(),
                                 nn.LazyLinear(num_outputs))

    def forward(self, X):
        return self.net(X)
    
    def loss(self, Y_hat, Y, averaged=True):
        Y_hat = Y_hat.reshape((-1, Y_hat.shape[-1]))
        Y = Y.reshape((-1,))
        return F.cross_entropy(
            Y_hat, Y, reduction='mean' if averaged else 'none')