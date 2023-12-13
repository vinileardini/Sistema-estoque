from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from PIL import ImageTk,Image
import awesometkinter as atk

class login():
    
    def __init__(self,master=None):
        
        mainLogin = Frame(master,background='#121212')
        mainLogin.pack()
        titleLogin = Label(mainLogin,text='InovaTech Master',font=('Arial',12),foreground='#ffffff',background='#121212')
        titleLogin.pack(pady=10)
        #Inserção imagem 
        img = PhotoImage(file='img\cpu.png')
        img = img.subsample(5,5)
        imgtitleLogin = Label(mainLogin,image=img,background='#121212')
        imgtitleLogin.image = img
        imgtitleLogin.pack()
        
        #Campo de entrada do nome de usuário
        userLabel = Label(mainLogin,background='#121212')
        userLabel.pack(pady=20)
        userField = Label(userLabel,text='Usuário:',foreground='#ffffff',background='#121212')
        userField.pack(side=LEFT)
        nameInput = Entry(userLabel,width=30)
        nameInput.pack(pady=20)
        
        #Campo de entrada de senha
        passwordLabel = Label(mainLogin,background='#121212')
        passwordLabel.pack(pady=10)
        passwordField = Label(passwordLabel,text='Senha:',foreground='#ffffff',background='#121212')
        passwordField.pack(padx=5,side=LEFT)
        passwordInput = Entry(passwordLabel,width=30)
        passwordInput.pack()
        
        #Botão para envio de dados de login
        buttonsLabel = Label(mainLogin,background='#121212')
        buttonsLabel.pack(pady=20)
        submitButton = atk.Button3d(buttonsLabel,text='Login',bg='#4278f5')
        submitButton.pack()
        
        

root = Tk()
root.geometry("300x300")
root.maxsize(400,400)
root.minsize(400,400)
root.config(background='#121212')
root.title("Área de login")
imgIcon = Image.open('img\cpu.png')
icon = ImageTk.PhotoImage(imgIcon)
root.wm_iconphoto(FALSE,icon)
login(root)
root.mainloop()