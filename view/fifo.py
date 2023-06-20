import tkinter as tk
from tkinter import ttk


class FifoFrame(ttk.Frame): 
    def __init__(self, parent):
        super().__init__(parent)

        self.memoria = 0
        self.paginas = []
        self.indice = 0

        # Creo estilos para el contenedor
        # Imagen de fondo
        self.background_image = tk.PhotoImage(file="media/fondo.png")
        styleContenedor = ttk.Style()
        styleContenedor.configure("Custom.TLabelframe", borderwidth=0)

        # creo el frame contenedor que depende del frame principal (ventana o self)
        self.frame = tk.Frame(parent)

        # Creo el label con la imagen de fondo
        self.label_fondo = tk.Label(self.frame, image=self.background_image)

        # Configuración y contenido del frame
        self.boton = ttk.Button(self.frame, text="Vista de FIFO", cursor="hand2")
        self.boton.config(command=self.agregar_referencia_FIFO)

        self.label_referencia = ttk.Label(self.frame, text="Referencia:")
        self.entry_referencia = ttk.Entry(self.frame)
        self.boton_agregar_referencia = ttk.Button(self.frame, text="Agregar", cursor="hand2")
        self.boton_agregar_referencia.config(command=self.agregar_referencia_FIFO)

    def agregar_referencia_FIFO(self):
        referencia = self.entry_referencia.get().strip()
        if referencia:
            if referencia not in self.paginas:  # Verificar si la referencia ya existe en la lista de páginas
                if len(self.paginas) >= self.memoria:
                    self.paginas[self.indice] = referencia  # Reemplazar la página más antigua en el índice actual
                    self.indice = (self.indice + 1) % self.memoria  # Actualizar el índice circularmente
                else:
                    self.paginas.append(referencia)  # Agregar la nueva referencia al final de la lista
                self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())


    def mngFrame(self, funcion):
        if funcion:
            # Pinto el frame
            self.frame.pack(expand=True, fill=tk.BOTH)
            self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            self.boton.pack()

            # Crear estilo personalizado
            styleTable = ttk.Style()
            styleTable.configure("EstiloTabla.Treeview",
                                 background="#D3D3D3",
                                 foreground="black",
                                 fieldbackground="#D3D3D3",
                                 bordercolor="black",
                                 borderwidth=1,
                                 relief="solid")

            # Creo la tabla
            self.tree = ttk.Treeview(self.frame, style="EstiloTabla.Treeview", columns=('#0', 'Referencia'))
            # Oculto la primera columna
            self.tree.heading('#0')
            self.tree.column('#0', width=0, stretch=tk.NO)
            # Creo las columnas
            self.tree.heading('#1', text='Referencia', anchor='center')
            self.tree.column('#1', width=80, anchor='center')
            self.tree.place(x=100, y=100, width=300, height=250)

            self.actualizar_tabla()

            self.label_referencia.pack()
            self.entry_referencia.pack()
            self.boton_agregar_referencia.pack()

            # Añadir línea divisora entre columnas 1 y 2
            self.separator = ttk.Separator(self.frame, orient='vertical')
            self.separator.place(in_=self.tree, relx=1 / 2, rely=0, relheight=1)

        else:
            # Quito el frame
            self.frame.pack_forget()


# Crear ventana principal
ventana = tk.Tk()

# Crear instancia del frame FIFO
fifo_frame = FifoFrame(ventana)
ventana.mainloop()
