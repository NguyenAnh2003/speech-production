import torch
from omegaconf import DictConfig
from transformers import AutoProcessor
from .data_pipeline import DataPipeline


class ModelModules:
    def __init__(self, conf: DictConfig) -> None:
        self.conf = conf
        self.model = self.get_model()
        self.data_pipeline = DataPipeline(
            self.get_pretrained_processor()
        )  # get processor directly

    def get_pretrained_processor(self):
        _, processor = self._get_pretrained_model()
        return processor

    def _get_pretrained_model(model_name: str, use_nemo: bool):
        # init
        model = None
        processor = None

        # if use nemo toolkit
        if use_nemo:
            # nemo pipeline
            pass
        else:
            # hf pipeline
            pass

        return model, processor

    def get_model(self):
        try:
            model = None
            if self.conf.is_pretrained:
                model, _ = self._get_pretrained_model(
                    self.conf.pretrained_section.model_name,
                    self.conf.pretrained_section.use_nemo,
                )
            else:
                model = torch.load()
            return model
        except Exception as e:
            raise ValueError(e)

    def s2t_predict(self, input: torch.Tensor):
        processed_input = self.data_pipeline(input)
        out = self.model(processed_input)  # transcbie with nemo orelse
        return out
