from core.modules.model_modules import ModelModules
from omegaconf import OmegaConf

conf = OmegaConf.load("./configs/default.yaml")
print(conf)
model_module = ModelModules(conf=conf)


def s2t_sevice(file):
    try:
        result = model_module.s2t_predict(file)
        return result
    except Exception as e:
        raise ValueError(e)
