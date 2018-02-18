from tkinter import *
from tkinter import ttk

aken = Tk()
aken.title('Loo Kasutaja.')
aken.geometry('400x300+600+300')
aken.configure(background = '#42cef4')

ttk.Style().configure('AB.Tlabel', background = '#42cef4', foreground = 'green')
ttk.Style().configure('AB.TButton', background = '#f45f41', foreground = 'green')

id = StringVar()
salakood = StringVar()

raam = ttk.Frame(aken).grid(row = 0, column = 0)


aken.mainloop()