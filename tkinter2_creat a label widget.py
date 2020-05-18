# tkinter 2 creating a lable widget

from tkinter import *

window = Tk()

window.title('First')

lbl = Label(window, text = 'Hello')

lbl.grid(column=0,row=0)

window.mainloop()
