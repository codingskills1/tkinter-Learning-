# tkinter 20 Show warning and error messages

from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("First")

window.geometry("800x600")

def clicked():
    messagebox.showwarning("Warn", "Don't Click")

btn = Button(window, text = "Click Me", bg = "orange", fg = "red", command = clicked)

btn.grid(column=0,row=0)

window.mainloop()
