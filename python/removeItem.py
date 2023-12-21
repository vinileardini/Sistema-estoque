from tkinter import *
import tkinter as ttk
from tkinter.commondialog import Dialog
from tkinter import messagebox
from PIL import ImageTk,Image

class removeItem():
    
    def __init__(self,master=None):
        
        mainRemoveItem = Frame(master,background='#040f23')
        mainRemoveItem.pack()
        labelItem = Label(mainRemoveItem,background='#040f23')
        labelItem.pack(pady=20)
        itemField = Label(labelItem,text="Item:",background='#040f23',foreground='#ffffff')
        itemField.pack(pady=20,side=LEFT)
        self.itemInput = Entry(labelItem,width=30)
        self.itemInput.pack(pady=20,side=LEFT,padx=10)
        
        searchImage = PhotoImage(file='img/lupa.png')
        searchImage = searchImage.subsample(30,30)
        buttonSearchItem = Button(labelItem,image=searchImage,background='#040f23',command=lambda:self.searchItem())
        buttonSearchItem.image = searchImage
        buttonSearchItem.pack(side=RIGHT)
        
        infoLabel = Label(mainRemoveItem,background='#040d23')
        infoLabel.pack(pady=10)
        # Linha tracejada
        canvas = Canvas(infoLabel,background='#040d23',width=500,height=10,highlightthickness=0)
        canvas.create_line(500,5,10,5,dash=(8,2),fill='#ffffff')
        canvas.pack()
        
        # Display de informações do item pesquisado
        infoField = Label(infoLabel,background='#040d23',foreground='#ffffff',text='Informações do item',font=('Arial',14))
        infoField.pack(pady=20)
        labelId = Label(infoLabel,background='#040d23',foreground='#ffffff')
        labelId.pack(pady=10)
        idField =  Label(labelId,text='ID:',background='#040d23',foreground='#ffffff')
        idField.pack(side=LEFT,padx=8)
        self.textString = StringVar()
        self.idLabel = Entry(labelId,background='#040d23',foreground='#ffffff',state='readonly',readonlybackground='#040d23',textvariable=self.textString)
        self.idLabel.pack(side=RIGHT)
        labelItem = Label(infoLabel,background='#040d23',foreground='#ffffff')
        labelItem.pack(pady=10)
        itemField = Label(labelItem,text='Item:',background='#040d23',foreground='#ffffff')
        itemField.pack(side=LEFT,padx=2)
        self.itemLabel = Entry(labelItem,background='#040d23',foreground='#ffffff',state='readonly',readonlybackground='#040d23',textvariable=self.textString)
        self.itemLabel.pack(side=RIGHT)
        labelLocal = Label(infoLabel,background='#040d23',foreground='#ffffff')
        labelLocal.pack(pady=10)
        localField = Label(labelLocal,background='#040d23',foreground='#ffffff',text='Local:')
        localField.pack(side=LEFT)
        self.localLabel = Entry(labelLocal,background='#040d23',foreground='#ffffff',state='readonly',readonlybackground='#040d23',textvariable=self.textString)
        self.localLabel.pack(side=RIGHT)
        labelButtons = Label(infoLabel,background='#040d23',foreground='#ffffff')
        labelButtons.pack(pady=20)
        confirmButton = Button(labelButtons,text='✔ Confirmar',background='#02c202',command=lambda:self.confirmRemove())
        confirmButton.pack(padx=10,side=LEFT)
        cancelButton = Button(labelButtons,text='❌ Excluir',background='#eb1313',command=lambda:self.cancelRemove())
        cancelButton.pack()
        
    
    def searchItem(self):
        
        item = self.itemInput.get()
        
        self.itemInput.delete(0,'end')
        
        self.textString.set(item)
        
    
    def confirmRemove(self):
        
        try:
            messagebox.showinfo('Remoção de item','O item foi removido com sucesso')
            
            self.textString.set('')
    
        except:
            messagebox.showerror('Remoção de item','Não foi possível realizar a remoção do item')
            
            self.textString.set('')
        
    
    def cancelRemove(self):
        
        try:
            self.itemInput.delete(0,'end')
            messagebox.showinfo('Remoção de item','A remoção do item foi cancelada com sucesso')
            
            self.textString.set('')
    
        except:
            messagebox.showwarning('Remoção de item','Não foi possível concluir a remoção do item')
            
            self.textString.set('')
    
            
        
        
        
        
        
        
        
        
        

root = Tk()
root.config(background='#040f23')
root.maxsize(300,500)
root.minsize(300,500)
root.title('Remoção de item')
imgIcon = Image.open('img\\boxcrate.png')
icon = ImageTk.PhotoImage(imgIcon)
root.wm_iconphoto(FALSE,icon)
removeItem(root)
root.mainloop()
        