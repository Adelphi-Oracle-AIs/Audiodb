class AudioDataset:
    def __init__(self, name):
        self.name = name
        self.audio_files = []

    def add_file(self, audio_file):
        self.audio_files.append(audio_file)

    def remove_file(self, audio_file):
        self.audio_files.remove(audio_file)

    def to_huggingface_dataset(self):
        # Convert to Hugging Face Dataset format
        pass
