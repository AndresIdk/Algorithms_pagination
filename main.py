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

algoritmo = 2  # Variable para guardar el algoritmo seleccionado
band = 0  # Variable para guardar el estado de la referencia
procesos = []  # Variable para guardar los procesos ingresados

def OnClickFifo():
    memoria = 0
    global algoritmo
    global band
    while(True):
        memoria = simpledialog.askstring("Memoria", "Ingrese marcos a utilizar (MAX 10):") # Variable para guardar los marcos de memoria disponibles
        if(memoria.isdigit()):
            if(int(memoria) <= 10):
                memoria = int(memoria)
                frames[0].memoria = memoria
                algoritmo = 0
                break
    changeStatusFIFO(estado, estadoAnterior)
    band = 0
    frames[0].indice = 0
    showInterfaces(estado, estadoAnterior, frames)

def OnClickLru():
    memoria = 0
    global algoritmo 
    global band

    while(True):
        memoria = simpledialog.askstring("Memoria", "Ingrese marcos a utilizar (MAX 10):") # Variable para guardar los marcos de memoria disponibles
        if(memoria.isdigit()):
            if(int(memoria) <= 10):
                memoria = int(memoria)
                frames[1].memoria = memoria
                algoritmo = 1
                break
    changeStatusLRU(estado, estadoAnterior)
    band = 0
    frames[1].indice = 0
    showInterfaces(estado, estadoAnterior, frames)

def algoritmoEjecutado():
    global band
    procesos = frames[0].actual.copy()
    if(not(algoritmo > 1 or algoritmo < 0)):
        if(algoritmo == 0):
            proceso = simpledialog.askstring("Procesos", "Ingrese proceso a ingresar")
            while(True):
                if(proceso.isdigit()):
                    proceso = int(proceso)
                    FIFO(frames[0], proceso, frames[0].indice, band)
                    band += 1
                    if(frames[0].indice >= frames[0].memoria - 1):
                        frames[0].indice = 0
                    else:
                        if not(proceso in [i for i in range(1, frames[0].memoria + 1)]):
                            if not(proceso in procesos):
                                frames[0].indice += 1
                    break
        else:
            proceso = simpledialog.askstring("Procesos", "Ingrese proceso a ingresar")
            while(True):
                if(proceso.isdigit()):
                    proceso = int(proceso)
                    LRU(frames[1], proceso, frames[1].indice, band)
                    band += 1
                    if(frames[1].indice >= frames[1].memoria - 1):
                        frames[1].indice = 0
                    else:
                        if not(proceso in [i for i in range(1, frames[1].memoria + 1)]):
                            if not(proceso in procesos):
                                frames[1].indice += 1
                    break
    else:
        label = tk.Label(ventana, text="Algoritmo no seleccionado", fg="red", font=("Times New Roman", 26))
        label.pack(pady=50)
        label.after(1500, label.destroy)


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

labelOpc = ttk.Label(cabeceraFrame, text="SELECCIONE UN ALGORITMO", font=("Helvetica", 14))
labelOpc.configure(style="TLabel", foreground="blue")
labelOpc.pack(side=tk.LEFT, padx=180, pady=5)

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

# Cargar la imagen
imagenI = Image.open("media/insert.png")
imagenI = ImageTk.PhotoImage(imagenI)

# Crear el botón y establecer la imagen de fondo
opcion1 = ttk.Button(ventana, command=algoritmoEjecutado, style="TButton", cursor="hand2", image=imagenI, padding=0)
opcion1.place(x=10, y=80, height=100, width=80)

# Cargar imagen
imagenL = Image.open("media/label.png")
imagenL = ImageTk.PhotoImage(imagenL)
# Crear label para el botón
LabelInsert = ttk.Label(ventana, image=imagenL, padding=0)
LabelInsert.place(x=25, y=180, width=50, height=50)

# Cargar imagen
imagenM = Image.open("media/memoria.png")
imagenM = ImageTk.PhotoImage(imagenM)

# Label para memoria ram
LabelMemoria = ttk.Label(ventana,image=imagenM, padding=-9, justify=tk.LEFT)
LabelMemoria.place(x=0, y=290, width=100, height=250)

# Crea frame contenedor
contenedor = ttk.Frame(ventana)
contenedor.place(width=884, height=548, x=105, y=48)

# Los frames contenedores de las vistas
frames = [FifoFrame(contenedor), LruFrame(contenedor)]

ventana.mainloop()
