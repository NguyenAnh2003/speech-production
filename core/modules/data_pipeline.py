import torchaudio


class DataPipeline:
    def __init__(self, processor) -> None:
        super.__init__(processor=processor)
        self.processor = processor

    def pipeline_s2t(self, input):
        try:
            preprocessed_data = None # preprocessed_data
            audio_array = torchaudio.load(input) # audio array
            preprocessed_data = self.processor(audio_array)
            return preprocessed_data      
        except Exception as e:
            raise ValueError(e)

    def pipeline_asr(self):
        pass
