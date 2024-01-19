from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image

from conexaobd import connectionDB

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
        
        # pesquisa do item 
        labelSearchId = Label(mainEdit,background='#040f23')
        labelSearchId.pack(pady=10)
        idSearchField = Label(labelSearchId,background='#040f23',text='ID:',foreground='#ffffff')
        idSearchField.pack(side=LEFT,padx=10)
        self.textEntryId = StringVar()
        self.idEntry = Entry(labelSearchId,textvariable=self.textEntryId)
        self.idEntry.pack(side=LEFT)
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(18,18)
        self.buttonSearchID = Button(labelSearchId,background='#040f23',image=searchImage,command=lambda:self.searchItem())
        self.buttonSearchID.image = searchImage
        self.buttonSearchID.pack(side=RIGHT,padx=5)
        
        # linha tracejada de divisória
        canvas = Canvas(mainEdit,background='#040d23',width=500,height=10,highlightthickness=0)
        canvas.create_line(500,5,10,5,dash=(8,2),fill='#ffffff')
        canvas.pack()
        
        # informações do item
        labelId = Label(mainEdit,background='#040f23')
        labelId.pack(pady=10)
        idField = Label(labelId,background='#040f23',foreground='#ffffff',text='Id:')
        idField.pack(side=LEFT,padx=10)
        self.idEntry = Entry(labelId,background='#040f23',foreground='#ffffff')
        self.idEntry.pack(side=LEFT)
        labelLocal = Label(mainEdit,background='#040f23')
        labelLocal.pack(pady=10)
        localField = Label(labelLocal,background='#040f23',foreground='#ffffff',text='Local:')
        localField.pack(side=LEFT,padx=10)
        self.textEntryLocal = StringVar()
        self.localEntry = Entry(labelLocal,background='#040f23',foreground='#ffffff',textvariable=self.textEntryLocal)
        self.localEntry.pack(side=LEFT)
        labelItem = Label(mainEdit,background='#040f23')
        labelItem.pack(pady=10)
        itemField = Label(labelItem,background='#040f23',foreground='#ffffff',text='Item:')
        itemField.pack(side=LEFT,padx=10)
        self.textEntryItem = StringVar()
        self.itemEntry = Entry(labelItem,background='#040f23',foreground='#ffffff',textvariable=self.textEntryItem)
        self.itemEntry.pack(side=LEFT)
        buttonsLabel = Label(mainEdit,background='#040f23')
        buttonsLabel.pack(pady=5)
        buttonConfirm = Button(buttonsLabel,background='#02c202',text='✔ Confirmar')
        buttonConfirm.pack(side=LEFT,padx=10)
        buttonCancel = Button(buttonsLabel,background='#eb1212',text='❌ Cancelar')
        buttonCancel.pack(side=LEFT)
        
    
    
    def placeholderID(self):
        
        if self.itemEntry.get() == '':
            self.textEntryId.set('Insira o id do item:')
        
        else:
            pass
    
    def searchItem(self):
        
        try:
        
            connection = connectionDB('estoque','')
            connection.connectDB()
            
            sql = ('SELECT patrimonioItem,tipoItem,localItem FROM items WHERE patrimonioItem = %s')
            value = self.idEntry.get()
            
            if value != '':
            
                connection.cursor.execute(sql,(value,))
                result = connection.cursor.fetchall()
                
                self.textEntryLocal.set(result[0][2])
                self.textEntryItem.set(result[0][1])
            
            else:
                print('Insira um id válido')
                
            
            connection.disconnectDB()
        
        except:
            messagebox.showerror('Edição de item','Não existe item com esse id')
    
    def resetSearch(self):
        
        try:
        
            self.textEntryId.set('')
            self.textEntryLocal.set('')
            self.textEntryItem.set('')
        except:
            print('não foi possivel limpar os campos')
        
        
        
        
        
        
        
        
        
        