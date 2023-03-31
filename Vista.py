from tkinter import *
from tkinter import ttk
import tkinter as tk
from Logica import *

cont = Logica()

def realizarRegistro():
    cont.guardarUsuarios(varNickname.get(), varMatricula.get(), varContrasena.get())

ventana = Tk()
ventana.title("Registro de Usuarios")
ventana.geometry("270x320")
ventana.resizable(0,0)
ventana.config(bg="lightblue")

#Crear un formulario para insertar datos en la tabla usuarios
titulo = Label(ventana, text="Registro de Usuarios", font=("Helvetica 16 bold"), bg="lightblue").place(x=10, y=10)
varNickname = tk.StringVar()
lblNickname = Label(ventana, text="Nickname", font=("Helvetica 12"), bg="lightblue").place(x=10, y=50)
txtNickname = Entry(ventana, textvariable=varNickname, font=("Helvetica 12"), width=20).place(x=10, y=70)
varMatricula = tk.StringVar()
lblMatricula = Label(ventana, text="Matricula", font=("Helvetica 12"), bg="lightblue").place(x=10, y=100)
txtMatricula = Entry(ventana, textvariable=varMatricula, font=("Helvetica 12"), width=20).place(x=10, y=120)
varContrasena = tk.StringVar()
lblContrasena = Label(ventana, text="Contraseña", font=("Helvetica 12"), bg="lightblue").place(x=10, y=150)
txtContrasena = Entry(ventana, textvariable=varContrasena, font=("Helvetica 12"), width=20, show = "*").place(x=10, y=170)

btnRegistrar = Button(ventana, text="Registrar", font=("Helvetica 11 bold"), bg="pink", command=realizarRegistro).place(x=90, y=220)

#Pestaña 2 - Consultar
titulo2 = Label(ventana, text="Consulta de Usuarios", font=("Helvetica 16 bold"), bg="lightblue").place(x=10, y=10)

varIdentificador = tk.StringVar()
lblIdentificador = Label(ventana, text="Identificador", font=("Helvetica 12"), bg="lightblue").place(x=10, y=50)
txtIdentificador = Entry(ventana, textvariable=varIdentificador, font=("Helvetica 12"), width=20).place(x=10, y=70)

btnBuscar = Button(ventana, text="Buscar", font=("Helvetica 11 bold"), bg="pink").place(x=90, y=220)

lblEncontrado = Label(ventana, text="Encontrado", font=("Helvetica 12"), bg="lightblue").place(x=10, y=50)
txtEncontrado = Entry(ventana, font=("Helvetica 12"), width=52, height=5).place(x=10, y=70)

#Pestaña 3 - Actualizar

ventana.mainloop()