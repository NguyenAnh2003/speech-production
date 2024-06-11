from core.modules.model_modules import ModelModules
from utils.utils import get_configs

conf = get_configs("./configs/default.yaml")
model_module = ModelModules(conf=conf)


def s2t_sevice(file):
    try:
        result = model_module.s2t_predict(file)
        return result
    except Exception as e:
        raise ValueError(e)
