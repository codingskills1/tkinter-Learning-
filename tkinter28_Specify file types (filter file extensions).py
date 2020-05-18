# tkinter 28 Specify file types (filter file extensions)
from tkinter import *
from tkinter import filedialog
from os import path

window = Tk()

window.title("First")

window.geometry("500x500")

def clicked():
    file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
    directory = filedialog.askdirectory()
btn = Button(window, text = "Open", command = clicked)

btn.grid(column = 0, row = 0)

window.mainloop()
