from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image

from conexaobd import connectionDB

class editItem(Toplevel):
    
    def __init__(self,master=None,update=None,setDropdownMenu=None):
        
        self.updateMenu = update
        self.dropdown = setDropdownMenu
        
        self.editItemWindow = ttk.Toplevel()
        imgIcon = Image.open('img\\cpu.png')
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
        labelSearchId.pack(pady=25)
        idSearchField = Label(labelSearchId,background='#040f23',foreground='#ffffff')
        idSearchField.pack(side=LEFT,padx=10)
        self.idEntry = Entry(labelSearchId,width=38)
        self.idEntry.insert(0,'Insira o id do item:')
        self.idEntry.bind('<Leave>',self.placeholderID)
        self.idEntry.bind('<Button-1>',self.excludePlaceholder)
        self.idEntry.pack(side=LEFT)
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(30,30)
        self.buttonSearchID = Button(labelSearchId,background='#040f23',image=searchImage,command=lambda:self.searchItem())
        self.buttonSearchID.image = searchImage
        self.buttonSearchID.pack(side=RIGHT,padx=5)
        
        # linha tracejada de divisória
        canvas = Canvas(mainEdit,background='#040d23',width=500,height=10,highlightthickness=0)
        canvas.create_line(500,5,10,5,dash=(8,2),fill='#ffffff')
        canvas.pack()
        
        # informações do item
        labelId = Label(mainEdit,background='#040f23')
        labelId.pack(pady=20)
        labelLocal = Label(mainEdit,background='#040f23')
        labelLocal.pack(pady=20)
        localField = Label(labelLocal,background='#040f23',foreground='#ffffff',text='Local:')
        localField.pack(side=LEFT,padx=8)
        self.textEntryLocal = StringVar()
        self.localEntry = Entry(labelLocal,background='#040f23',foreground='#ffffff',textvariable=self.textEntryLocal)
        self.localEntry.pack(side=RIGHT)
        labelItem = Label(mainEdit,background='#040f23')
        labelItem.pack(pady=20)
        itemField = Label(labelItem,background='#040f23',foreground='#ffffff',text='Item:')
        itemField.pack(side=LEFT,padx=10)
        self.textEntryItem = StringVar()
        self.itemEntry = Entry(labelItem,background='#040f23',foreground='#ffffff',textvariable=self.textEntryItem)
        self.itemEntry.pack(side=RIGHT)
        buttonsLabel = Label(mainEdit,background='#040f23')
        buttonsLabel.pack(pady=5)
        buttonConfirm = Button(buttonsLabel,background='#02c202',text='✔ Confirmar',command=lambda:self.alterItem())
        buttonConfirm.pack(side=LEFT,padx=15)
        buttonCancel = Button(buttonsLabel,background='#eb1212',text='❌ Cancelar',command=lambda:self.resetSearch())
        buttonCancel.pack()
        
        self.idItem = None
        self.tipoItem = None
        self.localItem = None
        
    # Exclui o placeholder do entry de ID
    
    def excludePlaceholder(self,*args):

        self.idEntry.delete(0,END)
        
    # Adiciona o placeholder no entry de ID
    
    def placeholderID(self,*args):
        if self.idEntry.get() != '':
            pass
        else:
            self.idEntry.insert(0,'Insira o ID do item:')
            
    # Realiza a busca de um determinado ID no banco de dados
    
    def searchItem(self):
        
        try:
        
            connection = connectionDB('estoque','')
            connection.connectDB()
            
            sql = ('SELECT patrimonioItem,tipoItem,localItem FROM items WHERE patrimonioItem = %s')
            value = self.idEntry.get()
            
            if value != '':
            
                connection.cursor.execute(sql,(value,))
                result = connection.cursor.fetchall()
                
                self.idItem = result[0][0]
                self.tipoItem = result[0][1]
                self.localItem = result[0][2]
                
                self.textEntryLocal.set(result[0][2])
                self.textEntryItem.set(result[0][1])
            
            else:
                print('Insira um id válido')
                
            
            connection.disconnectDB()
        
        except:
            messagebox.showerror('Edição de item','Não existe item com esse id')
    
    
    # Realiza a alteração do item no banco de dados
            
    def alterItem(self):
        
        try:
        
            connection = connectionDB('estoque','')
            connection.connectDB()
            
            if self.tipoItem != self.textEntryItem.get() or self.localItem != self.textEntryLocal.get():
                
                print('entrou')
                
                sql = ('UPDATE items SET tipoItem = %s, localItem = %s WHERE patrimonioItem = %s')
                
                print('id:',self.idItem)
                
                connection.cursor.execute(sql,(self.textEntryItem.get(),self.textEntryLocal.get(),self.idItem))
                connection.connection.commit()
                
                if connection.commitBD:
                    self.editItemWindow.destroy()
                    self.editItemWindow.after(0,self.updateMenu())
                    self.editItemWindow.after(0,self.dropdown())
                    print('Alteração realizada')

                else:
                    print('Não foi possível alterar o item')
            
            else:
                print('n entrou')
                
        except Exception as e:
            print(f'Não foi possível realizar a edição do item: {e}')
            connection.connection.rollback()
        
        connection.disconnectDB()
    
    
    
    def resetSearch(self):
        
        try:
            self.textEntryLocal.set('')
            self.textEntryItem.set('')
        except:
            print('não foi possivel limpar os campos')
        
        
        
        
        
        
        
        
        
        