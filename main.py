import tkinter as tk
from tkinter import ttk, simpledialog
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
from functions.algortimos import FIFO, LRU  # Modulo de algoirtmos

from view.fifo import FifoFrame  # Modulo de la vista de fifo
from view.lru import LruFrame  # Modulo de la vista de lru

from functions.helpers import (
    changeStatusFIFO,
    changeStatusLRU,
)  # Modulo de funciones auxiliares para cambio de estado
from functions.helpers import (
    showInterfaces,
)  # Modulo de funciones auxiliares para cambio de estado

def OnClickFifo():
    while(True):
        memoria = simpledialog.askstring("Memoria", "Ingrese marcos a utilizar (MAX 10):") # Variable para guardar los marcos de memoria disponibles
        if(memoria.isdigit()):
            if(int(memoria) <= 10):
                memoria = int(memoria)
                frames[0].memoria = memoria
                break
    changeStatusFIFO(estado, estadoAnterior)
    showInterfaces(estado, estadoAnterior, frames)

def OnClickLru():
    while(True):
        memoria = simpledialog.askstring("Memoria", "Ingrese marcos a utilizar (MAX 10):") # Variable para guardar los marcos de memoria disponibles
        if(memoria.isdigit()):
            if(int(memoria) <= 10):
                memoria = int(memoria)
                frames[1].memoria = memoria
                break
    changeStatusLRU(estado, estadoAnterior)
    showInterfaces(estado, estadoAnterior, frames)


# Crear la ventana principal y configurarla
ventana = tk.Tk()
ventana.title("Algoritmos de reemplazo de páginas")
ventana.geometry("1000x600")
ventana.resizable(False, False)
ventana.iconbitmap("media/icon.ico")

# Variable para guardar el estado del botón
estado = tk.IntVar(value=0)  # Inicia con la intefaz de inicio
estadoAnterior = tk.IntVar(value=0)

# Crear la cabecera con botones
cabeceraFrame = ttk.Frame(ventana)
cabeceraFrame.pack(side=tk.TOP, fill=tk.X)

opcFifo = ttk.Button(cabeceraFrame, command=OnClickFifo, text="FIFO", cursor="hand2")
opcFifo.pack(side=tk.LEFT, padx=10, pady=5)

opcLru = ttk.Button(cabeceraFrame, command=OnClickLru, text="LRU", cursor="hand2")
opcLru.pack(side=tk.LEFT, padx=10, pady=5)

# Crear la línea divisora
lineaFrame = ttk.Frame(ventana, height=2)
lineaFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
lineaFrame.configure(style="Horizontal.TSeparator")

# Crear el menú vertical
menuFrame = ttk.Frame(ventana)
menuFrame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=5)
# Crear la línea divisoria
separator = ttk.Separator(ventana, orient=tk.VERTICAL)
separator.place(x=100, y=45, rely=0, height=600)

# Se aplican estilos
style = ThemedStyle(ventana)
style.set_theme("arc")

opcion1 = ttk.Button(menuFrame, text="INSERT", command=FIFO, style="TButton", cursor="hand2")
opcion1.pack(pady=10)

opcion2 = ttk.Button(menuFrame, text="DELETE", command=LRU, style="TButton", cursor="hand2")
opcion2.pack(pady=10)

# Crea frame contenedor
contenedor = ttk.Frame(ventana)
contenedor.place(width=884, height=548, x=105, y=48)

# Los frames contenedores de las vistas
frames = [FifoFrame(contenedor), LruFrame(contenedor)]

ventana.mainloop()
