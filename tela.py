#impor de bibliotecas 
from tkinter import *
from tkinter import ttk
import time

# construçao da janela 
master = Tk()
master.title("login")
master.geometry("490x560+610+153")
#master.iconbitmap(default="icones/ico.ico")
master.resizable(width=1, height=1)


#def nova janela
def nova():
    
    master.destroy()
    time.sleep(0.3)
    master1 = Tk()
    master1.title("operação fechada")
    master1.geometry("490x560+610+153")
    
   
  

#var para esconder a senha
esconder = StringVar()

# import img
img_fundo = PhotoImage(file="img/fundo.png")
img_entrar = PhotoImage(file="img/entrar.png")

#label
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()


#input
en_usuario = Entry(master, bd=2, font=("arial", 16), justify=CENTER)
en_usuario.place(width = 287.7, height = 38.4, x= 105.7, y=216.3)

en_senha = Entry(master, textvariable=esconder, show="*", bd=2, font=("arial", 16), justify=CENTER)
en_senha.place(width = 287.7, height = 40.2, x=105.7 , y=302.7)

#textvariable=esconder, show="*" :: para esconder a senha

#button
bt_entrar = Button(master, bd=0,image= img_entrar, command=nova)
bt_entrar.place(width = 147, height = 52.6, x=176 , y=441.6)

#command=nova :: para chamar a nova janela

master.mainloop() #fazer o cod rodar