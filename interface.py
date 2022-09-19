import tkinter as tk

class App(tk.Tk):
    
	def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # coords = 100, 80, 400, 400
        # width = 500
        # height = 300
        #self.root = Tk()
        self.wm_title("Guitar Tuner")
        self.cnvs = tk.Canvas(self, width=500, height=300)
        self.cnvs.grid(row=2, column=1)
        # Create a background arc and pointer
        self.cnvs.create_arc(coord, start=0, extent=180, fill="white",  width=0, style='arc') 
        self.needle = self.cnvs.create_arc(100, 80, 400, 400)
        # Add labels
        self.cnvs.create_text(250, 10, font="Times 20 italic bold", text="GuitarTuner")
        self.low_txt = self.cnvs.create_text(70, 230, font="Times 12 bold", text="")
        self.mid_txt = self.cnvs.create_text(250, 60, font="Times 16 bold", text="")
        self.upp_txt = self.cnvs.create_text(430, 230, font="Times 12 bold", text="")
        self.freq_txt = self.cnvs.create_text(250, 260, font="Times 12", text="")
        self.action_txt = self.cnvs.create_text(0, 0, text="")

    def start(self):
        self.mainloop()

    def Update(self, id_note, target_note, max_freq):
        """ General update when a tone is played """
        pre_note = NOTES[id_note-1]
        pre_freq = NOTES_FREQS[id_note-1]
        pos_note = NOTES[id_note+1]
        pos_freq = NOTES_FREQS[id_note+1]
        target_freq = NOTES_FREQS[id_note]
        # Initialize needle and text
        self.cnvs.itemconfig(self.needle, start=0, extent=0)
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
        self.cnvs.itemconfig(self.needle, start=needle_start, extent=0)
        
    def UpdateRed(self, action, xcoord):
        """ Updates when actual note is not target note """
        self.cnvs.itemconfig(self.cnvs.needle, fill="red", outline='red', width=3)
        self.cnvs.itemconfig(self.cnvs.mid_txt, fill="black")
        self.cnvs.coords(self.cnvs.action_txt, xcoord, 100)
        self.cnvs.itemconfig(self.cnvs.action_txt, text=action)
        
    def UpdateGreen(self):
        """ Updates when actual note is target note """
        self.cnvs.itemconfig(self.cnvs.needle, fill="green", outline='green', width=3)
        self.cnvs.itemconfig(self.cnvs.mid_txt, fill="green") 

if __name__ == "__main__":
    app = App()
    app.start()