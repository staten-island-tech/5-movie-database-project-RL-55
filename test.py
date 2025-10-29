import tkinter
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=500)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=10, row=20)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=100, row=200)
root.mainloop()