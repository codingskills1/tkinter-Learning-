# tkinter 15 Get radio button value (selected radio button)

from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("First")

window.geometry("500x500")

selected = IntVar()

r1 = Radiobutton(window, text = "First", value = 1, variable = selected)
r2 = Radiobutton(window, text = "Second", value = 2, variable = selected)
r3 = Radiobutton(window, text = "Third", value = 3, variable = selected)

def clicked():
    print(selected.get())

btn = Button(window, text="Click Me", command=clicked)

r1.grid(column=0,row=0)
r2.grid(column=1,row=0)
r3.grid(column=2,row=0)

btn.grid(column=3,row=0)

window.mainloop()
