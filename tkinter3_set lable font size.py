# tkinter 3 set lable font size

from tkinter import *

window = Tk()

window.title('First')

lbl = Label(window, text = 'Hello', font=("Arial Bold",10))

lbl.grid(column=0,row=0)

window.mainloop()
