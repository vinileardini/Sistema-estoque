from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from PIL import ImageTk,Image

class newItem():
    
    def __init__(self,master=None):
        
        mainItem = Frame(master,background='#121212')
        mainItem.pack()
        labelItem = Label(mainItem,background='#121212')
        labelItem.pack(pady=20)
        itemField = Label(labelItem,text="Item:",background='#121212',foreground='#ffffff')
        itemField.pack(pady=20,side=LEFT)
        itemInput = Entry(labelItem,width=30)
        itemInput.pack(pady=20)
        labelCategory = Label(mainItem,background='#121212')
        labelCategory.pack(pady=20)
        categoryField = Label(labelCategory,text="Categoria:",background='#121212',foreground='#ffffff')
        categoryField.pack(pady=20,side=LEFT)
        categoryInput = Entry(labelCategory,width=30)
        categoryInput.pack(pady=20)
        labelQuantity = Label(mainItem,background='#121212')
        labelQuantity.pack(pady=20)
        quantityField = Label(labelQuantity,text="Quantidade:",background='#121212',foreground='#ffffff')
        quantityField.pack(pady=20,side=LEFT)
        quantityInput = Entry(labelQuantity,width=30)
        quantityInput.pack(pady=20)
        labelButtons = Label(mainItem,background='#121212')
        labelButtons.pack(pady=20)
        imgCheck = PhotoImage(file='img\check.png')
        displayCheck = imgCheck.subsample(25,25)
        confirmButton = Button(labelButtons,text='Confirmar',image=displayCheck,background='#02c202',compound=LEFT)
        confirmButton.pack()
        
        
        

root = Tk()
root.config(background='#121212')
root.maxsize(300,300)
root.minsize(300,400)
newItem(root)
root.mainloop()
