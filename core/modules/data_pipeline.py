import torchaudio
import torch


class DataPipeline:
    def __init__(self) -> None:
        pass

    def _load_audio_data(self, input):
        audio_array, rate = torchaudio.load(input)
        audio_array = torchaudio.functional.resample(audio_array, orig_freq=rate, new_freq=16000)
        return audio_array

    def pipeline_asr(self):
        pass
