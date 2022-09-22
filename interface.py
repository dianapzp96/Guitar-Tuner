from tkinter import Tk, Canvas
import config 

class App(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        coords = 100, 80, 500, 500
        self.wm_title("Guitar Tuner")
        self.cnvs = Canvas(self, width=600, height=400)
        self.cnvs.grid(row=3, column=1)
        # Create a background arc and pointer
        self.cnvs.create_arc(coords, start=0, extent=180, fill="white", width=3, style='arc') 
        self.needle = self.cnvs.create_arc(coords, start=0, extent=0)
        # Add labels
        #self.cnvs.create_text(300, 30, font="Times 20 italic bold", text="Guitar Tuner")
        self.low_txt = self.cnvs.create_text(100, 320, font="Times 22 bold", text="")
        self.mid_txt = self.cnvs.create_text(300, 60, font="Times 32 bold", text="")
        self.upp_txt = self.cnvs.create_text(500, 320, font="Times 22 bold", text="")
        self.freq_txt = self.cnvs.create_text(300, 320, font="Times 22", text="")
        self.action_txt = self.cnvs.create_text(80, 150, font="Times 18 bold", text="")

    def start(self):
        self.mainloop()

    def Update(self, id_note, target_note, max_freq):
        """ General update when a tone is played """
        pre_note = config.NOTES[id_note-1]
        pre_freq = config.NOTES_FREQS[id_note-1]
        pos_note = config.NOTES[id_note+1]
        pos_freq = config.NOTES_FREQS[id_note+1]
        target_freq = config.NOTES_FREQS[id_note]
        # Initialize needle and text
        #self.cnvs.itemconfig(self.needle, start=0, extent=0, width=3)
        self.cnvs.itemconfig(self.action_txt, text="")
        # Update notes labels
        self.cnvs.itemconfig(self.freq_txt ,text=str(round(max_freq,1)) + " Hz")
        self.cnvs.itemconfig(self.low_txt, text=pre_note)
        self.cnvs.itemconfig(self.mid_txt, text=target_note)
        self.cnvs.itemconfig(self.upp_txt, text=pos_note)
        # Update needle
        max_dist = max(abs(target_freq-pre_freq), abs(target_freq-pos_freq))
        start_freq = target_freq - max_dist
        end_freq = target_freq + max_dist
        needle_start = 180 * (end_freq - max_freq)/(end_freq - start_freq)
        self.cnvs.itemconfig(self.needle, start=needle_start, extent=0, width=3,
                            fill='black', outline='black')
        
    def UpdateRed(self, action, xcoord):
        """ Updates when actual note is not target note """
        self.cnvs.itemconfig(self.needle, fill="red", outline='red')
        self.cnvs.itemconfig(self.mid_txt, fill="black")
        self.cnvs.coords(self.action_txt, xcoord, 150)
        self.cnvs.itemconfig(self.action_txt, text=action)
        
    def UpdateGreen(self):
        """ Updates when actual note is target note """
        self.cnvs.itemconfig(self.needle, fill="green", outline='green')
        self.cnvs.itemconfig(self.mid_txt, fill="green")

if __name__ == "__main__":
    app = App()
    app.Update(id_note=0, target_note='C0', max_freq=0)
    app.start()