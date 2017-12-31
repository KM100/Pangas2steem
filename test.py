from tkinter import colorchooser
from tkinter import *
from tkinter import ttk
aken = Tk()
riikv = StringVar()
riik = ttk.Combobox(aken, textvariable=riikv)
riik['values'] = ('USA', 'Kanada', 'Austraalia')
riik.pack()
aken.mainloop()