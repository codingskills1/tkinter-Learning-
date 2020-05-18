# tkinter 5 adding a button widget

from tkinter import *

window = Tk()

window.title('First')

window.geometry('500x500')

lbl = Label(window, text = 'Hello', font=("Arial Bold",10))

lbl.grid(column=0,row=0)

btn = Button(window, text='Click Me')

btn.grid(column=1, row=0)

window.mainloop()
