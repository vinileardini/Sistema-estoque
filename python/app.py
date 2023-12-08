from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog

class app():
    master=None

    inicio = Frame(master,background='#121212')
    inicio.pack()

    teste = Label(inicio,text='TESTE')
    teste.pack()
    
root = Tk()
root.mainloop()