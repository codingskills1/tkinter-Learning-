# tkinter 25 Add a Progressbar widget
from tkinter import *
from tkinter.ttk import Progressbar 

window = Tk()

window.title("First")

window.geometry("500x500")

bar = Progressbar(window, length = 300)

bar['value'] = 30

bar.grid(column=0,row=0)

window.mainloop()
