import tkinter as tk
from tkinter import ttk


class FifoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Creo estilos para el contenedor
        # Imagen de fondo
        self.background_image = tk.PhotoImage(file="media/fondo.png")
        styleContenedor = ttk.Style()
        styleContenedor.configure("Custom.TLabelframe", borderwidth=0)

        # creo el frame contenedor que depende del frame principal (ventana o self)
        self.frame = tk.Frame(parent)

        # Creo el label con la imagen de fondo
        label_fondo = tk.Label(self.frame, image=self.background_image)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Configuración y contenido del frame
        self.boton = ttk.Button(self.frame, text="Vista de FIFO", cursor="hand2")

    def mngFrame(self, funcion):
        if funcion:
            # Pinto el frame
            self.frame.pack(expand=True, fill=tk.BOTH)
            self.boton.pack()

        else:
            # Quito el frame
            self.frame.pack_forget()
