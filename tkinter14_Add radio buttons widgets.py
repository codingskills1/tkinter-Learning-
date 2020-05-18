# tkinter 14 Add radio buttons widgets

from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("First")

window.geometry("500x500")

radio_state = BooleanVar()

radio_state.set(True)

r1 = Radiobutton(window, text = "First", value = 1, var=radio_state)
r2 = Radiobutton(window, text = "Second", value = 2)
r3 = Radiobutton(window, text = "Third", value = 3)

r1.grid(column=0,row=0)
r2.grid(column=1,row=0)
r3.grid(column=2,row=0)

window.mainloop()
