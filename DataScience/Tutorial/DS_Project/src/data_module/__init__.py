# Module information:
# - This folder contains the Python source codes used for generating, or downloading datasets which used for this project.
# File: __init__.py
# Functionality: Making ```data``` become a Python module
import torchvision
import torchvision.transforms as transforms
import torch
from d2l import torch as d2l


class DataModule(d2l.HyperParameters):  #@save
    """The base class of data."""
    def __init__(self, root='../data', num_workers=4):
        self.root = root
        self.num_workers = num_workers
        self.save_hyperparameters()

    def get_data(self, train):
        raise NotImplementedError

    def get_dataloader(self, train):
        dataset = self.get_data(train)
        return torch.utils.data.DataLoader(dataset, batch_size=self.batch_size, shuffle=True, num_workers=self.num_workers)
    
    def get_tensorloader(self, tensors, train, indices=slice(0, None)):
        tensors = tuple(a[indices] for a in tensors)
        dataset = torch.utils.data.TensorDataset(*tensors)
        return torch.utils.data.DataLoader(dataset, self.batch_size, shuffle=train)

class SyntheticRegressionData(DataModule):  #@save
    """Synthetic data for linear regression."""
    def __init__(self, w, b, noise=0.01, num_train=1000, num_val=1000, batch_size=32):
        super().__init__()
        self.save_hyperparameters()
        n = num_train + num_val
        self.X = torch.randn(n, len(w))
        noise = torch.randn(n, 1) * noise
        self.y = torch.matmul(self.X, w.reshape((-1, 1))) + b + noise
        
    def get_dataloader(self, train):
        i = slice(0, self.num_train) if train else slice(self.num_train, None)
        return self.get_tensorloader((self.X, self.y), train, i)
    
class Data(DataModule):
    def __init__(self, num_train, num_val, num_inputs, batch_size):
        self.save_hyperparameters()
        n = num_train + num_val
        self.X = torch.randn(n, num_inputs)
        noise = torch.randn(n, 1) * 0.01
        w, b = torch.ones((num_inputs, 1)) * 0.01, 0.05
        self.y = torch.matmul(self.X, w) + b + noise

    def get_dataloader(self, train):
        i = slice(0, self.num_train) if train else slice(self.num_train, None)
        return self.get_tensorloader([self.X, self.y], train, i)
    
class FashionMNIST(DataModule):
    def __init__(self, root, batch_size=64, resize=(28,28)):
        super().__init__(root, num_workers=4)
        self.batch_size = batch_size
        self.resize = resize
        self.train = self.get_data(train=True)
        self.test = self.get_data(train=False)

    def transform(self):
        return transforms.Compose([transforms.Resize(self.resize), transforms.ToTensor()])

    def get_data(self, train):
        return torchvision.datasets.FashionMNIST(root=self.root, train=train, transform=self.transform(), download=True)
    
    def train_dataloader(self):
        return self.get_dataloader(train=True)
    
    def val_dataloader(self):
        return self.get_dataloader(train=False)
    
    @staticmethod
    def text_labels(indices):
        labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
        return [labels[int(i)] for i in indices]