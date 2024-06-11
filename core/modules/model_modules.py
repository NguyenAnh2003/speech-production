import torch
from omegaconf import DictConfig, OmegaConf
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq, pipeline
from .data_pipeline import DataPipeline
from nemo.collections.asr.models.ctc_bpe_models import EncDecCTCModelBPE

class ModelModules:
    def __init__(self, conf: DictConfig) -> None:
        self.conf = OmegaConf.create(conf)
        self.model, self.processor = self.get_model_and_processor()
        self.data_pipeline = DataPipeline(
            processor=self.processor
        )  # get processor directly

    @staticmethod
    def _get_pretrained_model(model_name: str, use_nemo: bool):
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        # init
        processor = None

        # if use nemo toolkit
        if use_nemo:
            # nemo pipeline
            model = EncDecCTCModelBPE.from_pretrained(model_name)
        else:
            model = AutoModelForSpeechSeq2Seq.from_pretrained(
                model_name,
                torch_dtype=torch_dtype,
                low_cpu_mem_usage=True,
                use_safetensors=True,
            )
            processor = AutoProcessor.from_pretrained(model_name)
        model.cuda()

        return model, processor

    def get_model_and_processor(self):
        processor = None
        if self.conf.app.is_pretrained:
            model, processor = self._get_pretrained_model(
                self.conf.app.pretrained_section.model_name,
                self.conf.app.pretrained_section.use_nemo,
            )
        else:
            model = torch.load()

        return model, processor

    def s2t_predict(self, input: torch.Tensor):
        output = None
        if self.conf.app.pretrained_section.use_nemo == False:
            # using hf lib wil be init like this
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

        elif self.conf.app.pretrained_section.use_nemo == True:
            processed_input = self.data_pipeline._load_audio_data(input)
            processed_input = processed_input.squeeze(0)
            output = self.model.transcribe(processed_input) # transcbie with nemo orelse
            output = output[0] # just with nemo

        return output
