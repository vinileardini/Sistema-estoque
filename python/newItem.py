from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

class newItem():
    
    def __init__(self,master=None):
        
        mainItem = Frame(master,background='#040f23')
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
            connection = mysql.connector.connect(host='localhost',user='root',password='',database='estoque')
            cursor = connection.cursor()
            itemSearch = ('SELECT patrimonioItem FROM items')
            cursor.execute(itemSearch)
            result = cursor.fetchall()
            print(result)
            
            if patrimonioItem in result:
                messagebox.showwarning('Adição de item','Patrimônio já cadastrado')

            else:
                sql = ('INSERT INTO items(patrimonioItem,tipoItem,localItem) VALUES (%s,%s,%s)')
                values = (patrimonioItem,nomeItem,localItem)
                cursor.execute(sql,values)
                
                connection.commit()
        
                messagebox.showinfo(f'Item adicionado',f'O item {self.itemInput.get()} foi adicionado com sucesso')
                # Deleta as informações nos entrys
                self.itemInput.delete(0,'end')
                self.patrimonioInput.delete(0,'end')
                self.localInput.delete(0,'end')

        except:
            messagebox.showerror('Erro','Não foi possível adicionar o item')
            connection.rollback()
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
            
    
        

root = Tk()
root.config(background='#040f23')
root.maxsize(300,400)
root.minsize(300,400)
root.title('Adição de item')
imgIcon = Image.open('img\\boxcrate.png')
icon = ImageTk.PhotoImage(imgIcon)
root.wm_iconphoto(FALSE,icon)
newItem(root)
root.mainloop()
