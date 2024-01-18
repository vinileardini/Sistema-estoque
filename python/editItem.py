from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image

class editItem(Toplevel):
    
    def __init__(self,master=None,update=None,setDropdownMenu=None):
        
        
        self.editItemWindow = ttk.Toplevel()
        imgIcon = Image.open('img\\PC.png')
        icon = ImageTk.PhotoImage(imgIcon)
        self.editItemWindow.wm_iconphoto(False,icon)
        self.editItemWindow.title('Edição de item')
        self.editItemWindow.maxsize(300,400)
        self.editItemWindow.minsize(300,400)
        self.editItemWindow.config(background='#040f23')
        mainEdit = Frame(self.editItemWindow,background='#040f23')
        mainEdit.pack()
        labelId = Label(mainEdit,background='#040f23')
        labelId.pack(pady=10)
        idField = Label(labelId,background='#040f23',text='ID:',foreground='#ffffff')
        idField.pack(side=LEFT,padx=10)
        idEntry = Entry(labelId)
        idEntry.pack()
        labelLocal = Label(mainEdit,background='#040f23')
        labelLocal.pack(pady=10)
        localField = Label(labelLocal,background='#040f23',foreground='#ffffff',text='Local:')
        localField.pack(side=LEFT,padx=10)
        localEntry = Entry(labelLocal,background='#040f23')
        localEntry.pack()
        labelItem = Label(mainEdit,background='#040f23')
        labelItem.pack(pady=10)
        itemField = Label(labelItem,background='#040f23',foreground='#ffffff',text='Item:')
        itemField.pack(side=LEFT,padx=10)
        itemEntry = Entry(labelItem,background='#040f23',foreground='#ffffff')
        itemEntry.pack()
        
        
        
        
        
        