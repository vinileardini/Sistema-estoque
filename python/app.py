
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image

#Conexões do app
from newItem import newItem
from removeItem import removeItem


connection = mysql.connector.connect(host='localhost',user='root',password='',database='estoque')
cursor = connection.cursor()
    

class app():
    
    def __init__(self,master=None):
        
        self.root = root
    
        self.main = Frame(master,background='green')
        self.main.grid(row=0, column=0,sticky='nsew')
        self.title = Label(self.main,text='Sistema de gerenciamento de estoque',background='#040f23',foreground='#ffffff',font=('Arial',16))
        self.title.grid(column=0,row=0,sticky='ew')
        selectionMenu = Label(self.main,background='#040f23')
        selectionMenu.grid(column=0,row=1)
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        self.dropdownMenu = ttk.Combobox(selectionMenu,width=30)
        self.dropdownMenu['values'] = options
        self.dropdownMenu['state'] = 'readonly'
        self.dropdownMenu.set(options[1])
        self.dropdownMenu.grid(column=0,row=1)
        self.dropdownMenu.bind('<<ComboboxSelected>>',self.optionSelected)
        self.labelSearchItem = Entry(selectionMenu,width=50)
        self.labelSearchItem.grid(column=1,row=1,padx=10)
        self.labelSearchItem.insert(0,'Insira o patrimônio do item a ser pesquisado:')
        self.labelSearchItem.bind('<Button-1>',self.excludePlaceholder)
        self.labelSearchItem.bind('<Leave>',self.insertPlaceholder)
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(18,18)
        buttonSearchItem = Button(selectionMenu,image=searchImage,background='#040f23',command=lambda:self.searchItem())
        buttonSearchItem.image = searchImage
        buttonSearchItem.grid(column=2,row=1)
        self.labelDisplayMenu = tk.Label(self.main,pady=20,background='white',name='labelmenu')
        self.labelDisplayMenu.grid(column=0,row=2,sticky='nsew')
        scrollbarSide = tk.Scrollbar(self.labelDisplayMenu)
        scrollbarSide.grid(column=1,row=2,sticky='ns',pady=10)
       
        #Treeview style
        treeBodyStyle = ttk.Style()
        treeBodyStyle.theme_use('clam')
        treeBodyStyle.configure("body.Treeview",font=('Arial',12),background='#040f23',foreground='#ffffff',fieldbackground='#040f23')
        treeBodyStyle.configure("Treeview.Heading",background='#b3b3b3',font=('Arial',10))
        self.menu = ttk.Treeview(self.labelDisplayMenu,yscrollcommand=scrollbarSide.set,columns=("c1","c2","c3"),show='headings',style="body.Treeview",name='tree')
        self.menu.column("# 1",anchor=CENTER)
        self.menu.heading("# 1",text="Patrimônio")
        self.menu.column("# 2",anchor=CENTER)
        self.menu.heading("# 2",text="Local")
        self.menu.column("# 3",anchor=CENTER)
        self.menu.heading("# 3",text="Equipamento")
        self.menu.grid(column=0,row=2,sticky='nsew')
        self.menu.config(yscrollcommand=scrollbarSide.set)
        scrollbarSide.config(command=self.menu.yview)
       
    
        
        connection = mysql.connector.connect(host='localhost',user='root',password='',database='estoque')
        self.cursor = connection.cursor()
        
        self.itemsMenu()
        
        self.root.bind('<Configure>',self.windowSize)
        
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
                
                
            
            
    def optionSelected(self,event):
        
        option = self.dropdownMenu.get()
        
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        
        if option == options[0]:
            
            newItem()
        
        elif option == options[1]:
            
            pass
        
        else:
            
            removeItem()
        
        
    #Funções para o funcionamento do placeholder na entry de pesquisa de item
    
    def excludePlaceholder(self,*args):
        
        self.labelSearchItem.delete(0,END)
        
        
    def insertPlaceholder(self,*args):
        
        if self.labelSearchItem.get() != '':
            pass
        else:
            self.labelSearchItem.insert(0,'Insira o patrimônio do item a ser buscado:')
        
        
    def windowSize(self,event):
        
        self.main.config(width=event.width, height=event.height)
        
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        
        
        
        

       
        
        
        
        
        
        
    
    
    
    
        
        
root = Tk()
root.config(background='#040f23')
root.title('Sistema de gerenciamento de estoque')
root.maxsize(800,800)
root.minsize(300,300)
imgOpen = Image.open('img\logo.jpg')
imgOpen = imgOpen.resize((300,300))
img = ImageTk.PhotoImage(imgOpen)
root.wm_iconphoto(FALSE,img)
app(root)
root.mainloop()
        
        


