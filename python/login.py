from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from PIL import ImageTk,Image
import awesometkinter as atk

class login():
    
    def __init__(self,master=None):
        
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
        nameInput = Entry(userLabel,width=30)
        nameInput.pack(pady=20)
        
        #Campo de entrada de senha
        passwordLabel = Label(mainLogin,background='#040f23')
        passwordLabel.pack(pady=10)
        passwordField = Label(passwordLabel,text='Senha:',foreground='#ffffff',background='#040f23',font=('Arial',12))
        passwordField.pack(padx=5,side=LEFT)
        passwordInput = Entry(passwordLabel,width=30)
        passwordInput.pack()
        
        #Botão para envio de dados de login
        buttonsLabel = Label(mainLogin,background='#040f23')
        buttonsLabel.pack(pady=20)
        submitButton = atk.Button3d(buttonsLabel,text='Login',bg='#121212')
        submitButton.pack()
        
        

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