from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog

class login():
    
    def __init__(self,master=None):
        
        mainLogin = Frame(master)
        mainLogin.pack()
        titleLogin = Label(mainLogin)
        imgtitleLogin = Label(image="D:\Sistema estoque\pc.png")
        imgtitleLogin.pack()
        

root = Tk()
login(root)
root.mainloop()
