# tkinter 21 Show warning and error messages

from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("First")

window.geometry("800x600")

def clicked():
    messagebox.showerror("error", "malvare detected")

btn = Button(window, text = "Click Me", bg = "orange", fg = "red", command = clicked)

btn.grid(column=0,row=0)

window.mainloop()
