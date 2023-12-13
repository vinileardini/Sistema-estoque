from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog

class app():
    
    def __init__(self,master=None):
    
        main = Frame(master)
        main.pack()
        title = Label(main,text='Sistema de gerenciamento de estoque')
        title.pack(pady=10)
        selectionMenu = Label(main)
        selectionMenu.pack()
        selectedOption = StringVar(value="Selecione uma opção")
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        buttonNewItem = OptionMenu(selectionMenu,selectedOption,*options)
        buttonNewItem.pack(side=LEFT,padx=10)
        labelSearchItem = Entry(selectionMenu,width=50)
        labelSearchItem.pack(side=LEFT,padx=10)
        buttonSearchItem = Button(selectionMenu)
        buttonSearchItem.pack(side=RIGHT,padx=10)
        
        
    
root = Tk()
root.config(background='#121212')
app(root)
root.mainloop()
