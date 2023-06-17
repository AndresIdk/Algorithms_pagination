import tkinter as tk
from tkinter import ttk

class LruFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Configuración y contenido del frame

        # creo el frame contenedor que depende del frame principal (ventana o self)
        self.frame = tk.Frame(parent)
        self.boton = ttk.Button(self.frame, text="Vista de LRU")
        
    def mngFrame(self, funcion):
        if funcion:
            # Pinto el frame
            self.frame.pack()
            self.boton.pack()
        else:
            # Quito el frame
            self.frame.pack_forget()