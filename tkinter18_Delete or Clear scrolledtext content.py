# tkinter 18 Delete/Clear scrolledtext content

from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

window = Tk()

window.title("First")

window.geometry("500x500")

txt = scrolledtext.ScrolledText(window,width = 10,height = 10)

txt.grid(column=0,row=0)

txt.insert(INSERT,"Your text goes here")

txt.delete(1.0,END)

window.mainloop()

