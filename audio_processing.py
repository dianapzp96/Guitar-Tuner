import numpy as np
import copy
import config

def DataProcessing(data):
    """ Organize format and length to perform FFT """
    data = np.frombuffer(data, dtype=np.int16)
    config.BUFFER[:-config.CHUNK] = config.BUFFER[config.CHUNK:]
    config.BUFFER[-config.CHUNK:] = data
    return config.BUFFER

def FFT(data):
    """ Fast Fourier Transform """
    # Fourier magnitude
    magnitudes = np.abs(np.fft.fft(data))
    magnitudes = magnitudes[:int(len(magnitudes) / 2)]
    # Harmonics
    magnitudes_ori = copy.deepcopy(magnitudes)
    for i in range(2, config.NUM_HARM+1, 1):
        hps_len = int(np.ceil(len(magnitudes) / i))
        magnitudes[:hps_len] *= magnitudes_ori[::i]  # multiply every i element
    # Fourier frequency
    frequencies = np.fft.fftfreq(int((len(magnitudes) * 2)/1), 1./config.RATE)
    return magnitudes, frequencies

def MaxFrequency(magnitudes, frequencies):
    """ Detects frequency of maximum magnitude """
    max_magn = np.amax(magnitudes)
    idx = np.where(magnitudes==max_magn)
    max_freq = frequencies[idx]
    max_freq = max_freq[max_freq>=0][0]
    return max_freq


def ClosestNote(max_freq):
    """ Get closests note from the actual tone """
    notes_freqs = np.array(config.NOTES_FREQS)
    idx = notes_freqs.searchsorted(max_freq)
    idx = np.clip(idx, 1, len(config.NOTES_FREQS)-1)
    left = notes_freqs[idx-1]
    right = notes_freqs[idx]
    idx -= max_freq - left < right - max_freq
    target_note = config.NOTES[idx]
    target_dist = max_freq - notes_freqs[idx]
    
    return idx, target_note, target_dist