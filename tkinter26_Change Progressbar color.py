# tkinter 26 Change Progressbar color
from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Progressbar

window = Tk()

window.title("First")

window.geometry("500x500")

style = ttk.Style()

style.theme_use("default")

style.configure("black.Horizontal.TProgressbar", background = "black")

bar = Progressbar(window, length = 200, style = "black.Horizontal.TProgressbar")

bar["value"] = 50

bar.grid(column=0,row=0)

window.mainloop()