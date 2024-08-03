import soundfile as sf
import numpy as np

def convert_audio_format(input_file, output_file, target_format):
    """
    Convert audio file to a different format.
    
    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the converted audio file.
        target_format (str): Desired output format (e.g., 'wav', 'mp3', 'flac').
    """
    data, samplerate = sf.read(input_file)
    sf.write(output_file, data, samplerate, format=target_format)

def convert_sample_rate(input_file, output_file, target_sample_rate):
    """
    Convert audio file to a different sample rate.
    
    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the converted audio file.
        target_sample_rate (int): Desired sample rate in Hz.
    """
    data, samplerate = sf.read(input_file)
    if samplerate != target_sample_rate:
        # Use a resampling library like resampy for high-quality resampling
        import resampy
        data = resampy.resample(data, samplerate, target_sample_rate)
    sf.write(output_file, data, target_sample_rate)
