
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
from conexaobd import connectionDB


connection = connectionDB('estoque','')
connection.connectDB()


class app():
    
    def __init__(self,master=None):
        
        self.root = root

        #Frame principal
        self.main = Frame(master,background='#040f23')
        self.main.pack(fill=BOTH)
        
        #Label do título
        self.title = Label(self.main,text='Sistema de gerenciamento de estoque',background='#040f23',foreground='#ffffff',font=('Arial',16))
        self.title.pack(fill=BOTH,pady=10)
        
        #Frame das opções de menu
        self.selectionMenu = Frame(self.main,background='#040f23')
        self.selectionMenu.pack()
        options = ["Adicionar Item","Pesquisar Item","Remover Item"]
        self.dropdownMenu = ttk.Combobox(self.selectionMenu,width=30)
        self.dropdownMenu['values'] = options
        self.dropdownMenu['state'] = 'readonly'
        self.dropdownMenu.set(options[1])
        self.dropdownMenu.pack(fill=X,side=LEFT,padx=15)
        self.dropdownMenu.bind('<<ComboboxSelected>>',self.optionSelected)
        
        #Entry para pesquisa do item
        self.entrySearchItem = Entry(self.selectionMenu,width=50)
        self.entrySearchItem.pack(fill=X,side=LEFT,padx=10)
        self.entrySearchItem.insert(0,'Insira o id do item a ser pesquisado:')
        self.entrySearchItem.bind('<Button-1>',self.excludePlaceholder)
        self.entrySearchItem.bind('<Leave>',self.insertPlaceholder)
        
        #Botão de pesquisa
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(18,18)
        buttonSearchItem = Button(self.selectionMenu,image=searchImage,background='#040f23',command=lambda:self.searchItem())
        buttonSearchItem.image = searchImage
        buttonSearchItem.pack(fill=X,side=LEFT,padx=3)
        
        #Menu treeview
        self.labelDisplayMenu = tk.Label(self.main,background='#040f23')
        self.labelDisplayMenu.pack(fill=BOTH)
        scrollbarSide = tk.Scrollbar(self.labelDisplayMenu)
        scrollbarSide.pack(side=RIGHT,fill=BOTH,pady=10)
       
        #Treeview style
        treeBodyStyle = ttk.Style()
        treeBodyStyle.theme_use('clam')
        treeBodyStyle.configure("body.Treeview",font=('Arial',12),background='#040f23',foreground='#ffffff',fieldbackground='#040f23')
        treeBodyStyle.configure("Treeview.Heading",background='#b3b3b3',font=('Arial',10))
        #Definições do treeview
        self.menu = ttk.Treeview(self.labelDisplayMenu,columns=("c1","c2","c3"),show='headings',style="body.Treeview")
        self.menu.heading("#1",text= "ID")
        self.menu.column("#1",anchor=CENTER)
        self.menu.heading("#2",text="Local")
        self.menu.column("#2",anchor=CENTER)
        self.menu.heading("#3",text="Equipamento")
        self.menu.column("#3",anchor=CENTER)
        self.menu.pack(pady=10)
        self.menu.config(yscrollcommand=scrollbarSide.set)
        scrollbarSide.config(command=self.menu.yview)
       
    
        
        #connection = mysql.connector.connect(host='localhost',user='root',password='Vini@_2003',database='estoque')
        #self.cursor = connection.cursor()
        
        self.itemsMenu()
        
        
        self.root.bind('<Configure>',self.windowSize)
        
    def itemsMenu(self):
    
        
        sql = ('SELECT patrimonioItem,tipoItem,localItem FROM items')
        
        #connection.cursor.execute(sql)
        
        connection.consultBD(sql)
        result = connection.result
        
        #result = connection.cursor.fetchall()
        
        for item in result:
            
            self.menu.insert('',0,values=(item[0],item[2],item[1]))
        
        
    def searchItem(self):
       
        try: 
        
            #Recebe o valor inserido no campo de entrada de pesquisa de item
            
            itemValue = self.entrySearchItem.get()
            
            #Busca no BD do patrimonio do item pesquisado
            
            sqlSearch = ('SELECT patrimonioItem,tipoItem,localItem FROM items WHERE patrimonioItem = %s')
            
            connection.cursor.execute(sqlSearch,itemValue)
            resultSearch = connection.cursor.fetchall()
            
            print(resultSearch)
            
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
            
            connection.cursor.execute('SELECT patrimonioItem,tipoItem,localItem from items')
            allItems = connection.cursor.fetchall()
            
            
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
        
        self.entrySearchItem.delete(0,END)
        
        
    def insertPlaceholder(self,*args):
        
        if self.entrySearchItem.get() != '':
            pass
        else:
            self.entrySearchItem.insert(0,'Insira o id do item a ser buscado:')
        
        
    def windowSize(self,event):
        
        self.menu.config(height=28)
        self.main.update_idletasks()
        
     
    
    
        
        
root = Tk()
root.config(background='#040f23')
root.title('Sistema de gerenciamento de estoque')
root.maxsize(700,800)
root.geometry('600x300')
root.minsize(300,300)
imgOpen = Image.open('img\logo.jpg')
imgOpen = imgOpen.resize((300,300))
img = ImageTk.PhotoImage(imgOpen)
root.wm_iconphoto(FALSE,img)
app(root)
root.mainloop()
        
        


