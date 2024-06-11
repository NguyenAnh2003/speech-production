import torch
from omegaconf import DictConfig
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq, pipeline
from .data_pipeline import DataPipeline


class ModelModules:
    def __init__(self, conf: DictConfig) -> None:
        self.conf = conf
        self.model = self.get_model()
        self.processor = self.get_pretrained_processor()
        self.data_pipeline = DataPipeline(
            processor=self.processor
        )  # get processor directly

    def get_pretrained_processor(self):
        _, processor = self._get_pretrained_model()
        return processor

    @staticmethod
    def _get_pretrained_model(model_name: str, use_nemo: bool):
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        # init
        model = None
        processor = None

        # if use nemo toolkit
        if use_nemo:
            # nemo pipeline
            pass
        else:
            model = AutoModelForSpeechSeq2Seq.from_pretrained(
                model_name,
                torch_dtype=torch_dtype,
                low_cpu_mem_usage=True,
                use_safetensors=True,
            )
            processor = AutoProcessor.from_pretrained(model_name)
        return model, processor

    def get_model(self):
        model = None
        if self.conf.is_pretrained:
            model, _ = self._get_pretrained_model(
                self.conf.pretrained_section.model_name,
                self.conf.pretrained_section.use_nemo,
            )
        else:
            model = torch.load()
        return model

    def s2t_predict(self, input: torch.Tensor):
        processed_input = None
        output = None
        if self.conf.pretrained_section.use_nemo == False:
            # init
            torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
            device = "cuda:0" if torch.cuda.is_available() else "cpu"

            processed_input = self.data_pipeline._load_audio_data(input=input)

            params = {
                "task": "automatic-speech-recognition",
                "model": self.model,
                "tokenizer": self.processor.tokenizer,
                "feature_extractor": self.processor.feature_extractor,
                "max_new_tokens": 128,
                "torch_dtype": torch_dtype,
                "device": device,
            }

            pipe = pipeline(**params)  # pipeline for processing input

            output = pipe(processed_input)

        elif self.conf.pretrained_section.use_nemo == False:
            processed_input = self.data_pipeline(input)
            output = self.model(processed_input)  # transcbie with nemo orelse
        return output
