# tkinter 19 Create a MessageBox

from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("First")

window.geometry("800x600")

def clicked():
    messagebox.showinfo("You Lose", "Play Again")

btn = Button(window, text = "Click Me", bg = "orange", fg = "red", command = clicked)

btn.grid(column=0,row=0)

window.mainloop()
