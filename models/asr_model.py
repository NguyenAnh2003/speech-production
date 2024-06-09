import torch
import torch.nn as nn

class ASRModel(nn.Module):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    
  def forward(self, x):
    pass