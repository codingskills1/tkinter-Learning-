# tkinter 27 Add a filedialog (file & directory chooser)
from tkinter import *
from tkinter import filedialog

window = Tk()

window.title("First")

window.geometry("500x500")

def clicked():
	file = filedialog.askopenfilename()

btn = Button(window, text = "Open", command = clicked)

btn.grid(column = 0, row = 0)

window.mainloop()
