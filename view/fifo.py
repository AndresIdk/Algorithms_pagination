import tkinter as tk
from tkinter import ttk

class FifoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame = tk.Frame(parent)
        self.frame.place(x=0, y=50, width=50, height=50)
        self.boton = ttk.Button(self.frame, text="Vista de FIFO")
        self.boton.place(x=0, y=50, width=50, height=50)
        # Configuración y contenido del frame

    def mngFrame(self, funcion):
        if funcion:
            # Pinto el frame
            self.frame.pack()
            self.boton.pack()
        else:
            # Quito el frame
            self.frame.pack_forget()
