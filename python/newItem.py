from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
from conexaobd import connectionDB


class newItem(Toplevel):
    
    def __init__(self,master=None):
        
        self.newItemWindow = ttk.Toplevel()
        imgIcon = Image.open('img\\PC.png')
        icon = ImageTk.PhotoImage(imgIcon)
        self.newItemWindow.wm_iconphoto(False,icon)
        self.newItemWindow.title('Adição de item')
        self.newItemWindow.maxsize(300,400)
        self.newItemWindow.minsize(300,400)
        self.newItemWindow.config(background='#040f23')
        mainItem = Frame(self.newItemWindow,background='#040f23')
        mainItem.pack()
        labelItem = Label(mainItem,background='#040f23')
        labelItem.pack(pady=20)
        itemField = Label(labelItem,text="Item:",background='#040f23',foreground='#ffffff')
        itemField.pack(pady=20,padx=15,side=LEFT)
        self.itemInput = Entry(labelItem,width=30)
        self.itemInput.pack(pady=20)
        labelPatrimonio = Label(mainItem,background='#040f23')
        labelPatrimonio.pack(pady=20)
        patrimonioField = Label(labelPatrimonio,text="Patrimonio:",background='#040f23',foreground='#ffffff')
        patrimonioField.pack(pady=20,side=LEFT)
        self.patrimonioInput = Entry(labelPatrimonio,width=30)
        self.patrimonioInput.pack(pady=20)
        labelLocal = Label(mainItem,background='#040f23')
        labelLocal.pack(pady=20)
        localField = Label(labelLocal,text="Local:",background='#040f23',foreground='#ffffff')
        localField.pack(pady=20,side=LEFT)
        self.localInput = Entry(labelLocal,width=30)
        self.localInput.pack(pady=20)
        labelButtons = Label(mainItem,background='#040f23')
        labelButtons.pack(pady=20)
        confirmButton = Button(labelButtons,text='✔ Confirmar',background='#02c202',command=lambda:self.addNewitem(self.itemInput.get(),self.patrimonioInput.get(),self.localInput.get()))
        confirmButton.pack(padx=10,side=LEFT)
        cancelButton = Button(labelButtons,text='❌ Excluir',background='#eb1313',command=lambda:self.cancelAdd())
        cancelButton.pack()
        
    
    # Confirmação de adição do item
    def addNewitem(self,nomeItem,patrimonioItem,localItem):
        try:
            
            connection = connectionDB('estoque','')
            connection.connectDB()
            
            #connection = mysql.connector.connect(host='localhost',user='root',password='Vini@_2003',database='estoque')
            cursor = connection.getCursor()
            itemSearch = ('SELECT patrimonioItem FROM items')
            connection.cursor.execute(itemSearch)
            result = connection.cursor.fetchall()
            print(f'Resultado:{result}')
            
            if patrimonioItem in result:
                messagebox.showwarning('Adição de item','Patrimônio já cadastrado')
                
                self.newItemWindow.destroy()

            else:
                sql = ('INSERT INTO items(patrimonioItem,tipoItem,localItem) VALUES (%s,%s,%s)')
                values = (patrimonioItem,nomeItem,localItem)
                connection.cursor.execute(sql,values)
                
                connection.commitBD()
                
                if connection.commitBD() == True:
                
                    print(connection.cursor.rowcount,'rows alterados')
                    messagebox.showinfo(f'Item adicionado',f'O item {self.itemInput.get()} foi adicionado com sucesso')
                
                # Deleta as informações nos entrys
                self.itemInput.delete(0,'end')
                self.patrimonioInput.delete(0,'end')
                self.localInput.delete(0,'end')

        except:
            messagebox.showerror('Erro','Não foi possível adicionar o item')
            
            self.itemInput.delete(0,'end')
            self.patrimonioInput.delete(0,'end')
            self.localInput.delete(0,'end')
    
    def cancelAdd(self):
        try:
            messagebox.showinfo(f'Cancelado','Foi cancelada a adição do item')
            self.itemInput.delete(0,'end')
            self.patrimonioInput.delete(0,'end')
            self.localInput.delete(0,'end')
        except:
            messagebox.showinfo('Cancelamento','Não foi possível cancelar a adição do item')
            self.itemInput.delete(0,'end')
            self.patrimonioInput.delete(0,'end')
            self.localInput.delete(0,'end')
            
    
        


