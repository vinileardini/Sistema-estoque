from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from PIL import ImageTk,Image

class newItem():
    
    def __init__(self,master=None):
        
        mainItem = Frame(master,background='#040f23')
        mainItem.pack()
        labelItem = Label(mainItem,background='#040f23')
        labelItem.pack(pady=20)
        itemField = Label(labelItem,text="Item:",background='#040f23',foreground='#ffffff')
        itemField.pack(pady=20,padx=15,side=LEFT)
        itemInput = Entry(labelItem,width=30)
        itemInput.pack(pady=20)
        labelCategory = Label(mainItem,background='#040f23')
        labelCategory.pack(pady=20)
        categoryField = Label(labelCategory,text="Categoria:",background='#040f23',foreground='#ffffff')
        categoryField.pack(pady=20,side=LEFT)
        categoryInput = Entry(labelCategory,width=30)
        categoryInput.pack(pady=20)
        labelQuantity = Label(mainItem,background='#040f23')
        labelQuantity.pack(pady=20)
        quantityField = Label(labelQuantity,text="Quantidade:",background='#040f23',foreground='#ffffff')
        quantityField.pack(pady=20,side=LEFT)
        quantityInput = Entry(labelQuantity,width=30)
        quantityInput.pack(pady=20)
        labelButtons = Label(mainItem,background='#040f23')
        labelButtons.pack(pady=20)
        confirmButton = Button(labelButtons,text='✔ Confirmar',background='#02c202')
        confirmButton.pack(padx=10,side=LEFT)
        cancelButton = Button(labelButtons,text='❌ Excluir',background='#eb1313')
        cancelButton.pack()
        
         
        

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
