import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from functions.algortimos import FIFO, LRU # Modulo de algoirtmos

from view.index import Home # Modulo de la vista de inicio
from view.fifo import FifoFrame # Modulo de la vista de fifo
from view.lru import LruFrame # Modulo de la vista de lru

from functions.helpers import changeStatusFIFO, changeStatusLRU # Modulo de funciones auxiliares para cambio de estado
from functions.helpers import showInterfaces # Modulo de funciones auxiliares para cambio de estado

def OnClickFifo():
    changeStatusFIFO(estado, estadoAnterior)
    showInterfaces(estado, estadoAnterior, frames)

def OnClickLru():
    changeStatusLRU(estado, estadoAnterior)
    showInterfaces(estado, estadoAnterior, frames)

# Crear la ventana principal y configurarla
ventana = tk.Tk()
ventana.title("Algorigmos de reemplazo de páginas")
ventana.geometry("1000x600")
ventana.resizable(False, False)

# Variable para guardar el estado del botón
estado = tk.IntVar(value=0) #Inicia con la intefaz de inicio
estadoAnterior = tk.IntVar(value=0)

# Crear la cabecera con botones
cabeceraFrame = ttk.Frame(ventana)
cabeceraFrame.pack(side=tk.TOP, fill=tk.X)

opcFifo = ttk.Button(cabeceraFrame, command=OnClickFifo, text="FIFO")
opcFifo.pack(side=tk.LEFT, padx=10, pady=5)

opcLru = ttk.Button(cabeceraFrame, command=OnClickLru, text="LRU")
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

opcion1 = ttk.Button(menuFrame, text="FIFO", command=FIFO, style="TButton")
opcion1.pack(pady=10)

opcion2 = ttk.Button(menuFrame, text="LRU", command=LRU, style="TButton")
opcion2.pack(pady=10)

# Creo estilos para el contenedor
# Imagen de fondo
background_image = tk.PhotoImage(file="media/fondo.png")
styleContenedor = ttk.Style()
styleContenedor.configure('Custom.TLabelframe', borderwidth=0)

# Crea frame contenedor
contenedor = ttk.LabelFrame(ventana, style='Custom.TLabelframe')
contenedor.place(width=884, height=548, x=105, y=45)
contenedor.pack()

# background_label = tk.Label(contenedor, image=background_image)
# background_label.pack(fill='both', expand=True)
# background_label.lower()

# Los frames contenedores de las vistas
frames = [Home(contenedor), FifoFrame(contenedor), LruFrame(contenedor)]


ventana.mainloop()



