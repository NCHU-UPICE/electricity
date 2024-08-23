
import torch 
from torch.utils.data import DataLoader
from Dataset import Electricity

model_pth = r''

model = torch.load(model_pth)

dataset = Electricity()

loader = DataLoader(dataset)

for batch in loader:
    x, y = batch

    pred_y = model(y)

    

