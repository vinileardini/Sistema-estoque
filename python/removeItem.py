from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from PIL import ImageTk,Image

class removeItem():
    
    def __init__(self,master=None):
        
        mainRemoveItem = Frame(master,background='#040f23')
        mainRemoveItem.pack()
        labelItem = Label(mainRemoveItem,background='#040f23')
        labelItem.pack(pady=20)
        itemField = Label(labelItem,text="Item:",background='#040f23',foreground='#ffffff')
        itemField.pack(pady=20,padx=15,side=LEFT)
        itemInput = Entry(labelItem,width=30)
        itemInput.pack(pady=20)
        infoLabel = Label(mainRemoveItem,background='#040d23')
        infoLabel.pack(pady=40)
        labelId = Label(infoLabel,background='#040d23',foreground='#ffffff')
        labelId.pack(pady=10)
        idField =  Label(labelId,text='ID:',background='#040d23',foreground='#ffffff')
        idField.pack(side=LEFT)
        idLabel = Label(labelId,background='#040d23',foreground='#ffffff',text='teste')
        idLabel.pack(side=RIGHT)
        labelItem = Label(infoLabel,background='#040d23',foreground='#ffffff')
        labelItem.pack(pady=10)
        itemField = Label(labelItem,text='Item:',background='#040d23',foreground='#ffffff')
        itemField.pack(side=LEFT)
        itemLabel = Label(labelItem,background='#040d23',foreground='#ffffff',text='teste')
        itemLabel.pack(side=RIGHT)
        labelLocal = Label(infoLabel,background='#040d23',foreground='#ffffff')
        labelLocal.pack(pady=10)
        localField = Label(labelLocal,background='#040d23',foreground='#ffffff',text='Local:')
        localField.pack(side=LEFT)
        localLabel = Label(labelLocal,background='#040d23',foreground='#ffffff',text='teste')
        localLabel.pack(side=RIGHT)
        
        
        
        

root = Tk()
root.config(background='#040f23')
root.maxsize(300,400)
root.minsize(300,400)
root.title('Remoção de item')
imgIcon = Image.open('img\\boxcrate.png')
icon = ImageTk.PhotoImage(imgIcon)
root.wm_iconphoto(FALSE,icon)
removeItem(root)
root.mainloop()
        