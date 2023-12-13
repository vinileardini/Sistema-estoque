from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog

class app():
    
    def __init__(self,master=None):
    
        main = Frame(master,background='#121212')
        main.pack()
        title = Label(main,text='Sistema de gerenciamento de estoque',background='#121212',foreground='#ffffff')
        title.pack(pady=10)
        selectionMenu = Label(main,background='#121212')
        selectionMenu.pack()
        selectedOption = StringVar(value="Selecione uma opção")
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        dropdownMenu = OptionMenu(selectionMenu,selectedOption,*options)
        dropdownMenu.config(bg='#121212',fg='#ffffff',activebackground='#121212',activeforeground='#ffffff')
        dropdownMenu["menu"].config(bg='#121212',fg='#ffffff',activebackground='#121212',activeforeground='#ffffff')
        dropdownMenu["highlightthickness"] = 0
        dropdownMenu.pack(side=LEFT,padx=10)
        labelSearchItem = Entry(selectionMenu,width=50)
        labelSearchItem.pack(side=LEFT,padx=10)
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(10,10)
        buttonSearchItem = Button(selectionMenu,image=searchImage,background='#121212')
        buttonSearchItem.image = searchImage
        buttonSearchItem.pack(side=RIGHT,padx=10)
        
        
    
root = Tk()
root.config(background='#121212')
app(root)
root.mainloop()
