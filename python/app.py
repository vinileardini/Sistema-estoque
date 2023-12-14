from tkinter import *
from tkinter import ttk
from tkinter.commondialog import Dialog

class app():
    
    def __init__(self,master=None):
    
        main = Frame(master,background='#121212')
        main.pack()
        title = Label(main,text='Sistema de gerenciamento de estoque',background='#121212',foreground='#ffffff')
        title.pack(pady=10)
        selectionMenu = Label(main,background='#121212')
        selectionMenu.pack()
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        dropdownMenu = ttk.Combobox(selectionMenu,textvariable='Selecione uma opção')
        dropdownMenu['values'] = options
        dropdownMenu['state'] = 'readonly'
        dropdownMenu.set('Selecione uma opção')
        dropdownMenu.pack(side=LEFT,padx=10)
        labelSearchItem = Entry(selectionMenu,width=50)
        labelSearchItem.pack(side=LEFT,padx=10)
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(18,18)
        buttonSearchItem = Button(selectionMenu,image=searchImage,background='#121212')
        buttonSearchItem.image = searchImage
        buttonSearchItem.pack(side=RIGHT,padx=10)
        
        
    
root = Tk()
root.config(background='#121212')
root.minsize(300,300)
app(root)
root.mainloop()
