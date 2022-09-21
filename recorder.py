import numpy as np
import pyaudio
import config

class Recorder:
    
    def __init__(self, *args, **kwargs):
        audio = pyaudio.PyAudio()
        self.stream = audio.open(format=config.FORMAT,
                                channels=config.CHANNELS,
                                rate=config.RATE,
                                input=True,
                                output=True,
                                frames_per_buffer=config.CHUNK)