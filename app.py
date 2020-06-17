import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.good = ':)'
        self.neutral = ':l'
        self.negative = ':('
        self.create_widgets()

    def create_widgets(self):
        self.master.bind('<Return>', self.change_emote)

        self.emote = tk.Label(self, text=self.neutral)
        self.emote.grid(row=0, column=0)

        self.text_field = tk.Entry(self)
        self.text_field.grid(row=1)

    
    def change_emote(self, event):
        self.emote['text'] = self.negative

root = tk.Tk()
window = Window(master=root)
window.mainloop()