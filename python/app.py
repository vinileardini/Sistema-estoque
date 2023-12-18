from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.commondialog import Dialog

class app():
    
    def __init__(self,master=None):
    
        main = Frame(master,background='#040f23')
        main.pack()
        title = Label(main,text='Sistema de gerenciamento de estoque',background='#040f23',foreground='#ffffff',font=('Arial',16))
        title.pack(pady=10)
        selectionMenu = Label(main,background='#040f23')
        selectionMenu.pack()
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        dropdownMenu = ttk.Combobox(selectionMenu,textvariable='Selecione uma opção',width=30)
        dropdownMenu['values'] = options
        dropdownMenu['state'] = 'readonly'
        dropdownMenu.set('Selecione uma opção')
        dropdownMenu.pack(side=LEFT,padx=10)
        labelSearchItem = Entry(selectionMenu,width=50)
        labelSearchItem.pack(side=LEFT,padx=10)
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(18,18)
        buttonSearchItem = Button(selectionMenu,image=searchImage,background='#040f23')
        buttonSearchItem.image = searchImage
        buttonSearchItem.pack(side=RIGHT,padx=10)
        labelDisplayMenu = tk.Label(main,pady=20,background='#040f23')
        labelDisplayMenu.pack()
        scrollbarSide = tk.Scrollbar(labelDisplayMenu)
        scrollbarSide.pack(side=RIGHT,fill=Y)
        scrollbarUnder = tk.Scrollbar(labelDisplayMenu,orient=HORIZONTAL)
        scrollbarUnder.pack(side=BOTTOM,fill=X)
        treeStyle = ttk.Style()
        treeStyle.theme_use('clam')
        treeStyle.configure("Treeview",font=('Arial',12),background='#040f23')
        # Estilo para os heading da treeview
        treeStyle.configure("Treeview.Heading",background='#b3b3b3',font=('Arial',10))
        menu = ttk.Treeview(labelDisplayMenu,yscrollcommand=scrollbarSide.set,xscrollcommand=scrollbarUnder.set,columns=("c1","c2","c3"),show='headings')
        menu.column("# 1",anchor=CENTER)
        menu.heading("# 1",text="Patrimônio")
        menu.column("# 2",anchor=CENTER)
        menu.heading("# 2",text="Local")
        menu.column("# 3",anchor=CENTER)
        menu.heading("# 3",text="Equipamento")
        menu.pack(side=LEFT,pady=20,padx=10)
        scrollbarSide.config(command=menu.yview)
        scrollbarUnder.config(command=menu.xview)
        
        
        
    
root = Tk()
root.config(background='#040f23')
root.minsize(300,300)
app(root)
root.mainloop()
