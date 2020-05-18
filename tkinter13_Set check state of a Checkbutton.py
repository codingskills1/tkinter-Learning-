# tkinter 13 Set check state of a Checkbutton
from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("First")

window.geometry("500x500")

chk_state = IntVar()

chk_state.set(0) # 0 is unchecked and 1 is checked

chk = Checkbutton(window, text = "True", var = chk_state)

chk.grid(column=0,row=0)

window.mainloop()
