import numpy as np
from interface import  App
from recorder import Recorder
import audio_processing
import config

audio = Recorder()

app = App()
app.resizable(0,0)   
running = True

def on_closing():
    global running
    running = False
    app.destroy()

def execution():
    if running:
        data = audio.stream.read(config.CHUNK)
        data = audio_processing.DataProcessing(data)
        magnitudes, frequencies = audio_processing.FFT(data)
        max_freq = audio_processing.MaxFrequency(magnitudes, frequencies)
        id_note, target_note, target_dist = audio_processing.ClosestNote(max_freq)
        app.Update(id_note, target_note, max_freq)

        if target_dist < -config.FREQ_THRESHOLD:
            xcoord = 80
            action = "TIGHTEN"
            app.UpdateRed(action, xcoord)
        elif target_dist > config.FREQ_THRESHOLD:
            xcoord = 520
            action = "LOOSEN"
            app.UpdateRed(action, xcoord)
        else:
            app.UpdateGreen()

        app.cnvs.update()
        app.protocol("WM_DELETE_WINDOW", on_closing)
        app.after(10, execution)

if __name__ == "__main__":
    execution()
    app.mainloop()

