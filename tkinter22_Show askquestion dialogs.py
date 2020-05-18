# tkinter 22 Show askquestion dialogs
from tkinter import messagebox

res = messagebox.askquestion("Question","bored or not")

res = messagebox.askyesno("Question","Happy or not")

res = messagebox.askokcancel("Question", "continue or cancel")

res = messagebox.askyesnocancel("Question", "yes or no")

res = messagebox.askokcancel("Question", "ok or cancel")

res = messagebox.askretrycancel("Question", "retry or cancel")


