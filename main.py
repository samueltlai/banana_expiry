import numpy as np
import torchvision.models.segmentation
import torch
import torchvision.transforms as tf

Learning_Rate=1e-5
width=height=900
batchSize=1


# loss function and optimiser
