import torchaudio
import torch


class DataPipeline:
    def __init__(self, processor) -> None:
        super.__init__()
        self.processor = processor

    def _load_audio_data(self, input):
        audio_array, rate = torchaudio.load(input)
        audio_array = torchaudio.functional.resample(audio_array, orig_freq=rate, new_freq=16000)
        return audio_array

    def pipeline_s2t(self, input):
        try:
            audio_array = self._load_audio_data(input=input)  # audio array
            audio_array = torch.mean(
                audio_array, dim=0
            )  # take mean where audio has 2 dimensions
            preprocessed_data = self.processor(audio_array)
            return preprocessed_data
        except Exception as e:
            raise ValueError(e)

    def pipeline_asr(self):
        pass
