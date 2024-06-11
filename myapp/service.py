from core.modules.model_modules import ModelModules
from omegaconf import OmegaConf


conf = OmegaConf.load("../../configs/default.yaml")

model_module = ModelModules(conf=conf)
model = model_module.get_model()

def s2t_sevice(file):
  # init model - predict here
  predict = model.translate() #?
  return file
