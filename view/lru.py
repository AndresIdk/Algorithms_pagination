import tkinter as tk
from tkinter import ttk

class LruFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Configuración y contenido del frame

        # Ejemplo de un botón dentro del frame
        self.boton = ttk.Button(self, text="Vista de LRU")
        self.boton.pack()