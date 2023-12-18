from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
from PIL import ImageTk,Image

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
        labelCategory = Label(mainItem,background='#040f23')
        labelCategory.pack(pady=20)
        categoryField = Label(labelCategory,text="Categoria:",background='#040f23',foreground='#ffffff')
        categoryField.pack(pady=20,side=LEFT)
        self.categoryInput = Entry(labelCategory,width=30)
        self.categoryInput.pack(pady=20)
        labelQuantity = Label(mainItem,background='#040f23')
        labelQuantity.pack(pady=20)
        quantityField = Label(labelQuantity,text="Quantidade:",background='#040f23',foreground='#ffffff')
        quantityField.pack(pady=20,side=LEFT)
        self.quantityInput = Entry(labelQuantity,width=30)
        self.quantityInput.pack(pady=20)
        labelButtons = Label(mainItem,background='#040f23')
        labelButtons.pack(pady=20)
        confirmButton = Button(labelButtons,text='✔ Confirmar',background='#02c202',command=lambda:self.addNewitem())
        confirmButton.pack(padx=10,side=LEFT)
        cancelButton = Button(labelButtons,text='❌ Excluir',background='#eb1313',command=lambda:self.cancelAdd())
        cancelButton.pack()
    
    # Confirmação de adição do item
    def addNewitem(self):
        try:
            messagebox.showinfo(f'Item adicionado',f'O item {self.itemInput.get()} foi adicionado com sucesso')
            # Deleta as informações nos entrys
            self.itemInput.delete(0,'end')
            self.categoryInput.delete(0,'end')
            self.quantityInput.delete(0,'end')
        except:
            messagebox.showerror('Erro','Não foi possível adicionar o item')
            self.itemInput.delete(0,'end')
            self.categoryInput.delete(0,'end')
            self.quantityInput.delete(0,'end')
    
    
    def cancelAdd(self):
        try:
            messagebox.showinfo(f'Cancelado','Foi cancelada a adição do item')
            self.itemInput.delete(0,'end')
            self.categoryInput.delete(0,'end')
            self.quantityInput.delete(0,'end')
        except:
            messagebox.showinfo('Cancelamento','Não foi possível cancelar a adição do item')
            self.itemInput.delete(0,'end')
            self.categoryInput.delete(0,'end')
            self.quantityInput.delete(0,'end')
            
    
        

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
