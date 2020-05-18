# tkinter 23 Add a SpinBox (numbers widget)
from tkinter import *

window = Tk()

window.title("First")

window.geometry("500x500")

spin = Spinbox(window , from_ = 0, to_ = 100, width = 10)

spin.grid(column=0,row=0)

window.mainloop()