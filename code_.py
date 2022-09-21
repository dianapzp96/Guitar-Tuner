import numpy as np
import copy
import pyaudio
from tkinter import *

# *** GLOBAL VARIABLES ***

NOTES = ['C0', 'C#0', 'D0', 'D#0', 'E0', 'F0', 'F#0', 'G0', 'G#0', 'A0', 'A#0', 'B0',
         'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1',
         'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2',
         'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3',
         'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4',
         'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5',
         'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6',
         'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7',
         'C8', 'C#8', 'D8', 'D#8', 'E8', 'F8', 'F#8', 'G8', 'G#8', 'A8', 'A#8', 'B8']
NOTES_FREQS = [16.35,17.32,18.35,19.45,20.60,21.83,23.12,24.50,25.96,27.50,29.14,30.87,
               32.70,34.65,36.71,38.89,41.20,43.65,46.25,49.00,51.91,55.00,58.27,61.74,
               65.41,69.30,73.42,77.78,82.41,87.31,92.50,98.00,103.8,110.0,116.5,123.5,
               130.8,138.6,146.8,155.6,164.8,174.6,185.0,196.0,207.7,220.0,233.1,246.9,
               261.6,277.2,293.7,311.1,329.6,349.2,370.0,392.0,415.3,440.0,466.2,493.9,
               523.3,554.4,587.3,622.3,659.3,698.5,740.0,784.0,830.6,880.0,932.3,987.8,
               1047,1109,1175,1245,1319,1397,1480,1568,1661,1760,1865,1976,
               2093,2217,2349,2489,2637,2794,2960,3136,3322,3520,3729,3951,
               4186,4435,4699,4978,5274,5588,5920,6272,6645,7040,7459,7902] # in Hz
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
BUFFER_TIMES = 100
NUM_HARM = 4
FREQ_THRESHOLD = 0.4


class Recorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.buffer = np.zeros(CHUNK * BUFFER_TIMES)

    def Record(self):
        self.stream = self.audio.open(format=FORMAT,
                                        channels=CHANNELS,
                                        rate=RATE,
                                        input=True,
                                        output=True,
                                        frames_per_buffer=CHUNK)





# def DataProcessing(data):
#     """ Organize format and length to perform FFT """
#     data = np.frombuffer(data, dtype=np.int16)
#     buffer[:-CHUNK] = buffer[CHUNK:]
#     buffer[-CHUNK:] = data
#     return buffer

# def FFT(data):
#     """ Fast Fourier Transform """
#     # Fourier magnitude
#     magnitudes = np.abs(np.fft.fft(data))
#     magnitudes = magnitudes[:int(len(magnitudes) / 2)]
    
#     # Harmonics
#     magnitudes_ori = copy.deepcopy(magnitudes)
#     for i in range(2, NUM_HARM+1, 1):
#         hps_len = int(np.ceil(len(magnitudes) / i))
#         magnitudes[:hps_len] *= magnitudes_ori[::i]  # multiply every i element

#     # Fourier frequency
#     frequencies = np.fft.fftfreq(int((len(magnitudes) * 2)/1), 1./RATE)
    
#     return magnitudes, frequencies

# def MaxFrequency(magnitudes, frequencies):
#     """ Detects frequency of maximum magnitude """
#     # Frequency of max. magnitude
#     max_magn = np.amax(magnitudes)
#     idx = np.where(magnitudes==max_magn)
#     max_freq = frequencies[idx]
#     max_freq = max_freq[max_freq>=0][0]
    
#     return max_magn, max_freq

# def ClosestNote(target_freq):
#     """ Get closests note from the actual tone """
#     #A must be sorted
#     notes_freqs = np.array(NOTES_FREQS)
#     idx = notes_freqs.searchsorted(target_freq)
#     idx = np.clip(idx, 1, len(NOTES_FREQS)-1)
#     left = notes_freqs[idx-1]
#     right = notes_freqs[idx]
#     idx -= target_freq - left < right - target_freq
#     note = NOTES[idx]
#     target_dist = target_freq - notes_freqs[idx]
    
#     return idx, note, target_dist