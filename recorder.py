class AudioProcesser:

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


    def DataProcessing(self.data):
        """ Organize format and length to perform FFT """
        self.data = np.frombuffer(self.data, dtype=np.int16)
        self.buffer[:-CHUNK] = self.buffer[CHUNK:]
        self.buffer[-CHUNK:] = self.data
        # return self.buffer

    def FFT(data):
        """ Fast Fourier Transform """
        # Fourier magnitude
        self.magnitudes = np.abs(np.fft.fft(self.data))
        self.magnitudes = self.magnitudes[:int(len(self.magnitudes) / 2)]
        
        # Harmonics
        magnitudes_ori = copy.deepcopy(self.magnitudes)
        for i in range(2, NUM_HARM+1, 1):
            hps_len = int(np.ceil(len(self.magnitudes) / i))
            self.magnitudes[:hps_len] *= magnitudes_ori[::i]  # multiply every i element

        # Fourier frequency
        self.frequencies = np.fft.fftfreq(int((len(self.magnitudes) * 2)/1), 1./RATE)
        # return self.magnitudes, self.frequencies

    def MaxFrequency(magnitudes, frequencies):
        """ Detects frequency of maximum magnitude """
        # Frequency of max. magnitude
        self.max_magn = np.amax(self.magnitudes)
        idx = np.where(magnitudes==max_magn)
        self.max_freq = self.frequencies[idx]
        self.max_freq = self.max_freq[self.max_freq>=0][0]
        # return max_magn, max_freq

    def ClosestNote(target_freq):
        """ Get closests note from the actual tone """
        #A must be sorted
        notes_freqs = np.array(NOTES_FREQS)
        idx = notes_freqs.searchsorted(target_freq)
        idx = np.clip(idx, 1, len(NOTES_FREQS)-1)
        left = notes_freqs[idx-1]
        right = notes_freqs[idx]
        idx -= target_freq - left < right - target_freq
        note = NOTES[idx]
        target_dist = target_freq - notes_freqs[idx]
        
        return idx, note, target_dist