from abc import ABC, abstractmethod

class DataProvider(ABC):
    @abstractmethod
    def fetch_data(self, **kwargs):
        pass

class CommonVoiceProvider(DataProvider):
    def fetch_data(self, language='en', split='train'):
        # Implement fetching from Common Voice
        pass

class GigaSpeechProvider(DataProvider):
    def fetch_data(self, subset='XL'):
        # Implement fetching from GigaSpeech
        pass
