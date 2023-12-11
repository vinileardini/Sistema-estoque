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
        #img = ImageTk.PhotoImage(Image.open('img\PC_2.png'))
        #imgtitleLogin = Label(mainLogin,image=img,background='#121212')
        #imgtitleLogin.pack()
        userLabel = Label(mainLogin,background='#121212')
        userLabel.pack(pady=20)
        userField = Label(userLabel,text='Usuário:',foreground='#ffffff',background='#121212')
        userField.pack(side=LEFT)
        nameInput = Entry(userLabel,width=30)
        nameInput.pack(pady=20)
        passwordLabel = Label(mainLogin,background='#121212')
        passwordLabel.pack(pady=10)
        passwordField = Label(passwordLabel,text='Senha:',foreground='#ffffff',background='#121212')
        passwordField.pack(side=LEFT)
        passwordInput = Entry(passwordLabel,width=30)
        passwordInput.pack()
        buttonsLabel = Label(mainLogin,background='#121212')
        buttonsLabel.pack(pady=20)
        submitButton = atk.Button3d(buttonsLabel,text='Login',bg='#4278f5')
        submitButton.pack()
        
        

root = Tk()
root.geometry("300x300")
root.maxsize(300,300)
root.minsize(300,300)
root.config(background='#121212')
root.title("Área de login")
imgIcon = Image.open('img\cpu.png')
icon = ImageTk.PhotoImage(imgIcon)
root.wm_iconphoto(FALSE,icon)
login(root)
root.mainloop()