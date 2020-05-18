# tkinter 10 Disable entry widget
from tkinter import *

window = Tk()

window.title('First')

window.geometry('500x500')

lbl = Label(window, text = 'Hello', font=("Arial Bold",10))

lbl.grid(column=0,row=0)

txt = Entry(window, width = 10, state='disabled')

txt.grid(column=1,row=0)

txt.focus()

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

btn = Button(window, text='Click Me', bg = 'orange', fg = 'red', command = clicked)

btn.grid(column=2, row=0)

window.mainloop()
