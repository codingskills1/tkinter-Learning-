# tkinter 24 Set default value for Spinbox
from tkinter import *

window = Tk()

window.title("First")

window.geometry("500x500")

spin_state = IntVar()

spin_state.set(36)

spin = Spinbox(window, from_ = 0, to_ = 100, width = 5, textvariable = spin_state)

spin.grid(column = 0,row = 0)

window.mainloop()