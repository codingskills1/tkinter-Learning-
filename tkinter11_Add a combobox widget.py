# tkinter 11 Add a combobox widget
from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title('First')

window.geometry('500x500')

combo = Combobox(window)

combo['values'] = (1,2,3,4,5,6,'Text')

combo.current(3)

combo.get()

combo.grid(column=0,row=0)

window.mainloop()

