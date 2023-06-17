import tkinter as tk
from tkinter import ttk

class Home(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Configuración y contenido del frame
        self.frame = tk.Frame(parent)
        self.boton = ttk.Button(self.frame, text="Vista de HOME")
        
    def mngFrame(self, x):
        if x == 1:
            # creo el frame contenedor que depende del frame principal (ventana o self)
            self.frame.pack()
            # Ejemplo de un botón dentro del frame
            self.boton.pack()
        else:
            self.frame.pack_forget()
            self.boton.pack_forget()
        