import tkinter as tk
from tkinter import ttk

class FifoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Configuración y contenido del frame

        # creo el frame contenedor que depende del frame principal (ventana o self)
        self.frame = tk.Frame(self)
        self.frame.pack()
        # Ejemplo de un botón dentro del frame
        self.boton = ttk.Button(self.frame, text="Vista de FIFO")
        self.boton.pack()

    def getFrame(self):
        return self.frame
