from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from PIL import ImageTk,Image
import awesometkinter as atk
from tkinter import messagebox
import mysql.connector
from conexaobd import connectionDB
import menu

class login():
    
    def __init__(self,master=None):
        
        self.master = master
        self.userSigned = False
        
        mainLogin = Frame(master,background='#040f23')
        mainLogin.pack(side=RIGHT,padx=20)
        titleLogin = Label(mainLogin,text='InovaTech Master',font=('Arial',14),foreground='#ffffff',background='#040f23')
        titleLogin.pack(pady=10)
        
        #Inserção imagem 
        imgLogin  = Frame(master,height=400,width=250)
        imgLogin.pack(side=LEFT)
        imgOpen = Image.open('img\logo.jpg')
        imgOpen = imgOpen.resize((300,300))
        img = ImageTk.PhotoImage(imgOpen)
        imgtitleLogin = Label(imgLogin,image=img,background='#040f23')
        imgtitleLogin.image = img
        imgtitleLogin.pack()
        
        #Campo de entrada do nome de usuário
        userLabel = Label(mainLogin,background='#040f23')
        userLabel.pack(pady=20)
        userField = Label(userLabel,text='Usuário:',foreground='#ffffff',background='#040f23',font=('Arial',12))
        userField.pack(side=LEFT)
        self.nameInput = Entry(userLabel,width=30)
        self.nameInput.pack(pady=20)
        
        #Campo de entrada de senha
        passwordLabel = Label(mainLogin,background='#040f23')
        passwordLabel.pack(pady=10)
        passwordField = Label(passwordLabel,text='Senha:',foreground='#ffffff',background='#040f23',font=('Arial',12))
        passwordField.pack(padx=5,side=LEFT)
        self.passwordInput = Entry(passwordLabel,width=30,show='*')
        self.passwordInput.pack()
        
        
        #Botão para envio de dados de login
        
        buttonsLabel = Frame(mainLogin, background='#040f23')  # Use Frame instead of Label
        buttonsLabel.pack(pady=20)

        submitButton = atk.Button3d(buttonsLabel, text='Login', bg='#121212', command=lambda: self.loginUser(self.nameInput.get(), self.passwordInput.get()))
        submitButton.pack(fill=BOTH)
        
    def loginUser(self,nome,senha):
        
        try:
            
            connection = connectionDB('estoque','Vini@_2003')
            connection.connectDB()
            
            userBD = ('SELECT loginUser,passwordUser FROM users WHERE loginUser = %s AND passwordUser = %s')
            connection.cursor.execute(userBD,(nome,senha,))
            result = connection.cursor.fetchall()
            
            print(result)
            print(len(result))
            
            if len(result) > 0:
                        
                self.userSigned = True
                print('Usuário logado')
                self.master.destroy()
                self.execMenu()
                
                
                
            else:
                messagebox.showerror('Login','Usuário ou senha incorreta')
            
        except Exception as loginException:
            
            print(f'Não foi possível verificar o login: {loginException}')
    
    #Retorno para verificação se o usuário conseguiu ou não logar no app
    
    def signedOrNot(self):
        
        return self.userSigned
    
    # Função que altera o root para o menu e o executa
    
    def execMenu(self):
        
        root_menu = Tk()
        root_menu.config(background='#040f23')
        root_menu.title('Sistema de gerenciamento de estoque')
        root_menu.maxsize(700,800)
        root_menu.geometry('600x300')
        root_menu.minsize(300,300)
        imgOpen = Image.open('img\cpu.png')
        imgOpen = imgOpen.resize((300,300))
        img = ImageTk.PhotoImage(imgOpen)
        root_menu.wm_iconphoto(FALSE,img)

        menu.menu(root_menu)
        root_menu.mainloop()
    
            

root = Tk()
root.geometry("300x300")
root.maxsize(600,400)
root.minsize(600,400)
root.config(background='#040f23')
root.title("Área de login")
imgIcon = Image.open('img\cpu.png')
icon = ImageTk.PhotoImage(imgIcon)
root.wm_iconphoto(FALSE,icon)
login(root)
root.mainloop()
