from tkinter import *
from tkinter import ttk
from time import sleep
from random import randint

aknad = ''
aken = Tk()
aken.title('Logi sisse.')
aken.geometry('400x300+600+300')
aken.configure(background = '#42cef4')

def kontroll1():
    id2 = id.get()
    salakood2 = salakood.get()
    fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
    kasutajad = []
    for rida in fail:
        kasutajad.append(rida.strip('\n'))
    fail.close()
    for i in range(int(len(kasutajad)/4)):
        if kasutajad[i*4] == id2:
            nr = i*4
            kas = 'jah'
            break
        else:
            kas = 'ei'
    if kas == 'jah':
        if salakood2 == kasutajad[nr+2]:
            aken2 = Tk()
            aken2.title(kasutajad[nr+1].title())
            aken2.geometry('400x300+600+300')
            aken2.configure(background = '#42cef4')
            ttk.Style().configure('BC.TLabel', background = '#42cef4', foreground = 'green')
            ttk.Style().configure('BC.TButton', background = '#f45f41', foreground = 'green')
            raam = ttk.Frame(aken2).grid(row=0, column=0)
            l4 = ttk.Label(raam, text = 'KASUTAJA', style = 'BC.TLabel').grid(row = 0, column = 1, pady = 10, padx = 40)
            l5 = ttk.Label(raam, text = 'Konto omanik: ', style = 'BC.TLabel').grid(row = 1, column = 0, pady = 20, padx = 10)
            l6 = ttk.Label(raam, text = kasutajad[nr+1].title(), style = 'BC.TLabel', foreground = 'red').grid(row=1, column = 1, sticky = W, padx = 10)
            l7 = ttk.Label(raam, text = 'Kontol raha: ', style = 'BC.TLabel').grid(row = 2, column = 0, padx = 10)
            l8 = ttk.Label(raam, text = kasutajad[nr+3], style = 'BC.TLabel', foreground = 'red').grid(row = 2, column = 1, sticky = W)
            def välju():
                aken2.destroy()
            b2 = ttk.Button(raam, text = 'VÄLJU', style = 'BC.TButton', command = välju).grid(row = 3, column = 0, pady = 60)
            def mängi():
                aken2.destroy()
                aken3 = Tk()
                aken3.title('Mängud')
                aken3.geometry('400x300+600+300')
                aken3.configure(background = '#42cef4')
                ttk.Style().configure('DE.TLabel', background = '#42cef4', foreground = 'green')
                ttk.Style().configure('DE.TButton', background = '#f45f41', foreground = 'green')
                l11 = ttk.Label(raam, text = 'Mängud', font = ('arial', 18, 'bold'), foreground = 'black', style = 'DE.TLabel').grid(row = 0, column = 1, pady = 20, padx = 20)
                def arva():
                    s = 0
                    aken3.destroy()
                    number = randint(1, 100)
                    aken4 = Tk()
                    aken4.title('Arva Number')
                    aken4.geometry('400x300+600+300')
                    aken4.configure(background = '#42cef4')
                    ttk.Style().configure('EF.TLabel', background = '#42cef4', foreground = 'green')
                    ttk.Style().configure('EF.TButton', background = '#f45f41', foreground = 'green')
                    raam = ttk.Frame(aken4).grid(row = 0, column = 0)
                    l12 = ttk.Label(raam, text = 'ARVA', font = ('arial', 18, 'bold'), style = 'EF.TLabel').grid(row = 0, column = 1, pady = 30)
                    l13 = ttk.Label(raam, text = 'Sisestage arv 1-100', style = 'EF.TLabel').grid(row = 1, column = 0, pady = 20, padx = 20)
                    e3 = ttk.Entry(raam, width = 10, textvariable = s).grid(row = 1, column = 1)
                    def nr():
                        if int(s) < number:
                            l13 = ttk.Label(raam, text = 'ARV ON SUUREM', style = 'EF.TLabel', foreground = 'red', font = ('arial', 13, 'bold')).grid(row = 4, column = 0, pady = 20, padx = 40)
                        elif int(s) > number:
                            l13 = ttk.Label(raam, text = 'ARV ON VÄIKSEM', style = 'EF.TLabel', foreground = 'red', font = ('arial', 13, 'bold')).grid(row = 4, column = 0, pady = 20, padx = 40)
                        else:
                            kasutajad[nr+3]+=s
                            fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
                            for i in range(len(kasutajad)):
                                fail.write(str(kasutajad[i]))
                                fail.write('\n')
                            fail.close()
                            kontroll1()
                    ok_nupp = ttk.Button(raam, text = 'OK', style = 'EF.TButton', command = nr).grid(row = 2, column = 1, pady = 20, padx = 40)
                    aken4.mainloop()
                b4 = ttk.Button(raam, text = 'Arva number', style = 'DE.TButton', command = arva).grid(row = 1, column = 0, pady = 20, padx = 20)
            b3 = ttk.Button(raam, text = 'MÄNGIMA', style = 'BC.TButton', command = mängi).grid(row = 3, column = 1, pady = 60)
            aken2.mainloop()
        else:
            aken2 = Tk()
            aken2.title('ERROR')
            aken2.geometry('400x300+600+300')
            aken2.configure(background = '#42cef4')
            ttk.Style().configure('BC.TLabel', background = '#42cef4', foreground = 'green')
            ttk.Style().configure('BC.TButton', background = '#f45f41', foreground = 'green')
            raam = ttk.Frame(aken2).grid(row=0, column=0)
            l4 = ttk.Label(raam, font = ('arial', 18, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'ERROR').grid(row = 0, column = 0, pady = 20)
            l5 = ttk.Label(raam, font = ('arial', 13, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'VALE SALAKOOD').grid(row = 1, column = 0, pady = 40, padx = 120)
            def välju():
                aken2.destroy()
            b2 = ttk.Button(raam, text = 'VÄLJU', style = 'BC.TButton', command = välju).grid(row = 2, column = 1, pady = 60, sticky = E)
            aken2.mainloop()
    elif kas == 'ei':
        aken2 = Tk()
        aken2.title('ERROR')
        aken2.geometry('400x300+600+300')
        aken2.configure(background = '#42cef4')
        ttk.Style().configure('BC.TLabel', background = '#42cef4', foreground = 'green')
        raam = ttk.Frame(aken2).grid(row=0, column=0)
        l4 = ttk.Label(raam, font = ('arial', 18, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'ERROR').grid(row = 0, column = 0, pady = 20)
        l5 = ttk.Label(raam, font = ('arial', 13, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'KASUTAJAT EI TUVASTATUD').grid(row = 1, column = 0, pady = 40, padx = 70)
        aken2.mainloop()

def kontroll():
    aken.destroy()
    id2 = id.get()
    salakood2 = salakood.get()
    fail = open('jäätiskoer', 'r', encoding = 'UTF-8')
    kasutajad = []
    for rida in fail:
        kasutajad.append(rida.strip('\n'))
    fail.close()
    for i in range(int(len(kasutajad)/4)):
        if kasutajad[i*4] == id2:
            nr = i*4
            kas = 'jah'
            break
        else:
            kas = 'ei'
    if kas == 'jah':
        if salakood2 == kasutajad[nr+2]:
            aken2 = Tk()
            aken2.title(kasutajad[nr+1].title())
            aken2.geometry('400x300+600+300')
            aken2.configure(background = '#42cef4')
            ttk.Style().configure('BC.TLabel', background = '#42cef4', foreground = 'green')
            ttk.Style().configure('BC.TButton', background = '#f45f41', foreground = 'green')
            raam = ttk.Frame(aken2).grid(row=0, column=0)
            l4 = ttk.Label(raam, text = 'KASUTAJA', style = 'BC.TLabel').grid(row = 0, column = 1, pady = 10, padx = 40)
            l5 = ttk.Label(raam, text = 'Konto omanik: ', style = 'BC.TLabel').grid(row = 1, column = 0, pady = 20, padx = 10)
            l6 = ttk.Label(raam, text = kasutajad[nr+1].title(), style = 'BC.TLabel', foreground = 'red').grid(row=1, column = 1, sticky = W, padx = 10)
            l7 = ttk.Label(raam, text = 'Kontol raha: ', style = 'BC.TLabel').grid(row = 2, column = 0, padx = 10)
            l8 = ttk.Label(raam, text = kasutajad[nr+3], style = 'BC.TLabel', foreground = 'red').grid(row = 2, column = 1, sticky = W)
            def välju():
                aken2.destroy()
            b2 = ttk.Button(raam, text = 'VÄLJU', style = 'BC.TButton', command = välju).grid(row = 3, column = 0, pady = 60)
            def mängi():
                aken2.destroy()
                aken3 = Tk()
                aken3.title('Mängud')
                aken3.geometry('400x300+600+300')
                aken3.configure(background = '#42cef4')
                ttk.Style().configure('DE.TLabel', background = '#42cef4', foreground = 'green')
                ttk.Style().configure('DE.TButton', background = '#f45f41', foreground = 'green')
                l11 = ttk.Label(raam, text = 'Mängud', font = ('arial', 18, 'bold'), foreground = 'black', style = 'DE.TLabel').grid(row = 0, column = 1, pady = 20, padx = 20)
                def arva():
                    s = 0
                    aken3.destroy()
                    number = randint(1, 100)
                    aken4 = Tk()
                    aken4.title('Arva Number')
                    aken4.geometry('400x300+600+300')
                    aken4.configure(background = '#42cef4')
                    ttk.Style().configure('EF.TLabel', background = '#42cef4', foreground = 'green')
                    ttk.Style().configure('EF.TButton', background = '#f45f41', foreground = 'green')
                    raam = ttk.Frame(aken4).grid(row = 0, column = 0)
                    l12 = ttk.Label(raam, text = 'ARVA', font = ('arial', 18, 'bold'), style = 'EF.TLabel').grid(row = 0, column = 1, pady = 30)
                    l13 = ttk.Label(raam, text = 'Sisestage arv 1-100', style = 'EF.TLabel').grid(row = 1, column = 0, pady = 20, padx = 20)
                    e3 = ttk.Entry(raam, width = 10, textvariable = s).grid(row = 1, column = 1)
                    def nr():
                        if int(s) < number:
                            l13 = ttk.Label(raam, text = 'ARV ON SUUREM', style = 'EF.TLabel', foreground = 'red', font = ('arial', 13, 'bold')).grid(row = 4, column = 0, pady = 20, padx = 40)
                        elif s > number:
                            l13 = ttk.Label(raam, text = 'ARV ON VÄIKSEM', style = 'EF.TLabel', foreground = 'red', font = ('arial', 13, 'bold')).grid(row = 4, column = 0, pady = 20, padx = 40)
                        else:
                            kasutajad[nr+3]+=s
                            fail = open('jäätiskoer', 'w', encoding = 'UTF-8')
                            for i in range(len(kasutajad)):
                                fail.write(str(kasutajad[i]))
                                fail.write('\n')
                            fail.close()
                            kontroll1()
                    ok_nupp = ttk.Button(raam, text = 'OK', style = 'EF.TButton', command = nr).grid(row = 2, column = 1, pady = 20, padx = 40)
                b4 = ttk.Button(raam, text = 'Arva number', style = 'DE.TButton', command = arva).grid(row = 1, column = 0, pady = 20, padx = 20)
            b3 = ttk.Button(raam, text = 'MÄNGIMA', style = 'BC.TButton', command = mängi).grid(row = 3, column = 1, pady = 60)
            aken2.mainloop()
        else:
            aken2 = Tk()
            aken2.title('ERROR')
            aken2.geometry('400x300+600+300')
            aken2.configure(background = '#42cef4')
            ttk.Style().configure('BC.TLabel', background = '#42cef4', foreground = 'green')
            ttk.Style().configure('BC.TButton', background = '#f45f41', foreground = 'green')
            raam = ttk.Frame(aken2).grid(row=0, column=0)
            l4 = ttk.Label(raam, font = ('arial', 18, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'ERROR').grid(row = 0, column = 0, pady = 20)
            l5 = ttk.Label(raam, font = ('arial', 13, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'VALE SALAKOOD').grid(row = 1, column = 0, pady = 40, padx = 120)
            def välju():
                aken2.destroy()
            b2 = ttk.Button(raam, text = 'VÄLJU', style = 'BC.TButton', command = välju).grid(row = 2, column = 1, pady = 60, sticky = E)
            aken2.mainloop()
    elif kas == 'ei':
        aken2 = Tk()
        aken2.title('ERROR')
        aken2.geometry('400x300+600+300')
        aken2.configure(background = '#42cef4')
        ttk.Style().configure('BC.TLabel', background = '#42cef4', foreground = 'green')
        raam = ttk.Frame(aken2).grid(row=0, column=0)
        l4 = ttk.Label(raam, font = ('arial', 18, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'ERROR').grid(row = 0, column = 0, pady = 20)
        l5 = ttk.Label(raam, font = ('arial', 13, 'bold'), style = 'BC.TLabel', foreground = 'red', text = 'KASUTAJAT EI TUVASTATUD').grid(row = 1, column = 0, pady = 40, padx = 70)
        aken2.mainloop()

ttk.Style().configure('AB.TLabel', background = '#42cef4', foreground = 'green')
ttk.Style().configure('AB.TButton', background = '#f45f41', foreground = 'green')

id = StringVar()
salakood = StringVar()

raam = ttk.Frame(aken).grid(row=0, column=0)
l1 = ttk.Label(raam, text = 'SISSELOGIMINE', style = 'AB.TLabel').grid(row=0, column=1, pady = 10, padx = 40)
l2 = ttk.Label(raam, text = 'ID', style = 'AB.TLabel').grid(row=1, column=0, sticky = W, pady = 35, padx = 20)
e1 = ttk.Entry(raam, width=20, textvariable = id).grid(row=1, column=1)
l3 = ttk.Label(raam, text = 'SALAKOOD', style = 'AB.TLabel').grid(row=2, column=0, sticky = W, padx = 20)
e2 = ttk.Entry(raam, width=20, show = '*', textvariable = salakood).grid(row=2, column=1)
b1 = ttk.Button(raam, text = 'OK', style = 'AB.TButton', command = kontroll).grid(row = 3, column = 1, pady = 60)

aken.mainloop()
