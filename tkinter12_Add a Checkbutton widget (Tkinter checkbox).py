# tkinter 12 Add a Checkbutton widget (Tkinter checkbox)

from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("First")

window.geometry("500x500")

chk_state = BooleanVar()

chk_state.set(True)

chk = Checkbutton(window, text = "True",var = chk_state)

chk.grid(column = 0, row = 0)

window.mainloop()
