import torch
from omegaconf import DictConfig


class ModelModules:
    def __init__(self, conf: DictConfig) -> None:
        self.conf = conf

    def _get_pretrained_model(model_name: str, use_nemo: bool):
        if use_nemo:
            pass
        else:
            pass

    def get_model(self):
        # is_pretained from config
        model = None
        if self.conf.is_pretained:
            model = self._get_pretrained_model(
                self.conf.pretrained_section.model_name,
                self.conf.pretrained_section.use_nemo,
            )
        else:
            model = torch.load()
        return model
