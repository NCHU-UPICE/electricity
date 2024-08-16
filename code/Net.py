
import torch
from torch.nn import Module, Sequential
from torch.nn import Linear, BatchNorm1d, Flatten, Dropout, LayerNorm, Bilinear
from torch.nn import Conv1d
from torch.nn import Conv2d, BatchNorm2d, AvgPool2d, AdaptiveAvgPool2d, MaxPool2d
from torch.nn import Conv3d, BatchNorm3d, AvgPool3d, AdaptiveAvgPool3d
from torch.nn import ChannelShuffle
from torch.nn import GELU, ReLU, Mish, Sigmoid, Tanh

from torch.nn import LSTM, GRU

import torch.nn.functional as F

activation_function = GELU()

#---------------------------------------------------------------------------------------------------#
#                                                Net                                                #
#---------------------------------------------------------------------------------------------------#

class Net(Module):
    def __init__(self):
        super(Net, self).__init__()

        #------------------------------------#
        #          Hyperparameters           #
        #------------------------------------#

        layer_1_channels = 16
        layer_2_channels = 32
    
        #------------------------------------#
        #               Layers               #
        #------------------------------------#

        self.conv = Sequential(
            Conv2d(1, layer_1_channels, 3, 1, 1, bias = False),
            BatchNorm2d(layer_1_channels),
            GELU(),

            Conv2d(layer_1_channels, layer_2_channels, 3, 1, 1, bias = False),
            BatchNorm2d(layer_2_channels),
            GELU(),

            Flatten(),
            Linear(8192, 1),
        )


    def forward(self, x):

        #------------------------------------#
        #             Pipeline               #
        #------------------------------------#

        output = self.conv(x)
        return output 
