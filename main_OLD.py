class MainWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.file = None
        self.update()
        self.master.protocol('WM_DELETE_WINDOW', self.on_close)

    def open_file(self, filename="serial.txt"):
        if self.file is not None:
            self.file = open(filename)

    def update(self):
        if running:
            # update the widgets
            # reminder : when applicable, use tkinter variables
            # as they are easier to handle than manually updating with .config()
        self.after(1000, self.update)

    def on_close(self):
        self.file.close()
        self.file = None # can open again

running = True
root = Tk()
gui = MainWindow(root)
root.mainloop()