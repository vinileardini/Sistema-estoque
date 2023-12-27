from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
import mysql.connector

connection = mysql.connector.connect(host='localhost',user='root',password='',database='estoque')
cursor = connection.cursor()
    

class app():
    
    def __init__(self,master=None):
    
        main = Frame(master,background='#040f23')
        main.pack()
        title = Label(main,text='Sistema de gerenciamento de estoque',background='#040f23',foreground='#ffffff',font=('Arial',16))
        title.pack(pady=10)
        selectionMenu = Label(main,background='#040f23')
        selectionMenu.pack()
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        dropdownMenu = ttk.Combobox(selectionMenu,width=30)
        dropdownMenu['values'] = options
        dropdownMenu['state'] = 'readonly'
        dropdownMenu.set(options[1])
        dropdownMenu.pack(side=LEFT,padx=10)
        self.labelSearchItem = Entry(selectionMenu,width=50)
        self.labelSearchItem.pack(side=LEFT,padx=10)
        self.labelSearchItem.insert(0,'Insira o patrimônio do item a ser pesquisado:')
        self.labelSearchItem.bind('<Button-1>',self.excludePlaceholder)
        self.labelSearchItem.bind('<Leave>',self.insertPlaceholder)
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(18,18)
        buttonSearchItem = Button(selectionMenu,image=searchImage,background='#040f23')
        buttonSearchItem.image = searchImage
        buttonSearchItem.pack(side=RIGHT,padx=10)
        labelDisplayMenu = tk.Label(main,pady=20,background='#040f23')
        labelDisplayMenu.pack()
        scrollbarSide = tk.Scrollbar(labelDisplayMenu)
        scrollbarSide.pack(side=RIGHT,fill=Y)
        scrollbarUnder = tk.Scrollbar(labelDisplayMenu,orient=HORIZONTAL,background='#040f23')
        scrollbarUnder.pack(side=BOTTOM,fill=X)
       
        #Treeview style
        treeBodyStyle = ttk.Style()
        treeBodyStyle.theme_use('clam')
        treeBodyStyle.configure("body.Treeview",font=('Arial',12),background='#040f23',foreground='#ffffff',fieldbackground='#040f23')
        treeBodyStyle.configure("Treeview.Heading",background='#b3b3b3',font=('Arial',10))
        self.menu = ttk.Treeview(labelDisplayMenu,yscrollcommand=scrollbarSide.set,xscrollcommand=scrollbarUnder.set,columns=("c1","c2","c3"),show='headings',style="body.Treeview")
        self.menu.column("# 1",anchor=CENTER)
        self.menu.heading("# 1",text="Patrimônio")
        self.menu.column("# 2",anchor=CENTER)
        self.menu.heading("# 2",text="Local")
        self.menu.column("# 3",anchor=CENTER)
        self.menu.heading("# 3",text="Equipamento")
        self.menu.pack(side=LEFT,pady=20,padx=10)
        scrollbarSide.config(command=self.menu.yview)
        scrollbarUnder.config(command=self.menu.xview)
        buttonteste = Button(text='teste',command=self.itemsMenu())
        buttonteste.pack()
        button1 = Button(text='abc',command=lambda:self.searchItem())
        button1.pack()
        
        connection = mysql.connector.connect(host='localhost',user='root',password='Vini@_2003',database='estoque')
        self.cursor = connection.cursor()
        
        
    def itemsMenu(self):
    
        
        sql = ('SELECT patrimonioItem,tipoItem,localItem FROM items')
        
        cursor.execute(sql)
        result = cursor.fetchall()
        
        for item in result:
            
            self.menu.insert('',0,values=(item[0],item[2],item[1]))
        
        
    def searchItem(self):
       
        try: 
        
            #Recebe o valor inserido no campo de entrada de pesquisa de item
            
            itemValue = self.labelSearchItem.get()
            
            #Busca no BD do patrimonio do item pesquisado
            
            sqlSearch = ('SELECT patrimonioItem,tipoItem,localItem FROM items WHERE patrimonioItem = %s')
            
            cursor.execute(sqlSearch,(itemValue,))
            resultSearch = cursor.fetchall()
            
            result = self.menu.get_children()
            
            self.menu.insert('',0,values=(resultSearch[0][0],resultSearch[0][2],resultSearch[0][1]))
            
            for item in result:
                
                self.menu.delete(item)
        
        except:
            
            messagebox.showerror('Erro','Não existe item com essa identificação')
            
            menuElements = self.menu.get_children()
            
            for item in menuElements:
                
                self.menu.delete(item)
            
            # Inseri na treeview todos os itens existentes
            
            cursor.execute('SELECT patrimonioItem,tipoItem,localItem from items')
            allItems = cursor.fetchall()
            
            
            for itemDisplay in allItems:
                
                self.menu.insert('',0,values=(itemDisplay[0],itemDisplay[2],itemDisplay[1]))
                
                
            
            
            
                   
        
    #Funções para o funcionamento do placeholder na entry de pesquisa de item
    
    def excludePlaceholder(self,*args):
        
        self.labelSearchItem.delete(0,END)
        
        
    def insertPlaceholder(self,*args):
        
        if self.labelSearchItem.get() != '':
            pass
        else:
            self.labelSearchItem.insert(0,'Insira o patrimônio do item a ser buscado:')
        
        
        
        
        
        
        
        
        
        
        
        
        
    
root = Tk()
root.config(background='#040f23')
root.minsize(300,300)
app(root)
root.mainloop()
