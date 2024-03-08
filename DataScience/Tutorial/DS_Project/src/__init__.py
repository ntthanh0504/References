# Module information:
# - This folder contains the Python source codes used in this project.
# File: __init__.py
# Functionality: Making ```src``` become a Python module
import torch
import torch.nn as nn
from d2l import torch as d2l
import matplotlib.pyplot as plt

class ProgressBoard(d2l.HyperParameters):  #@save
    """The board that plots data points in animation."""
    def __init__(self, xlabel=None, ylabel=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 ls=['-', '--', '-.', ':'], colors=['C0', 'C1', 'C2', 'C3'],
                 fig=None, axes=None, figsize=(3.5, 2.5), display=True):
        self.save_hyperparameters()
        if fig is None or axes is None:
            self.fig, self.axes = plt.subplots(figsize=figsize)
        else:
            self.fig, self.axes = fig, axes
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.set_xscale(xscale)
        self.axes.set_yscale(yscale)
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)
        self.ls = ls
        self.colors = colors
        self.display = display

    def draw(self, x, y, label, every_n=1):
        if hasattr(x, '__iter__'):  # Check if x is iterable
            if len(x) % every_n == 0:
                self.axes.plot(x, y, linestyle=self.ls[0], color=self.colors[0], label=label)
                if self.display:
                    self.fig.canvas.draw()
                    plt.pause(0.01)
        else:
            self.axes.plot(x, y, linestyle=self.ls[0], color=self.colors[0], label=label)
            if self.display:
                self.fig.canvas.draw()
                plt.pause(0.01)