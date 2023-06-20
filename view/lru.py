import tkinter as tk
from tkinter import ttk


class LruFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.memoria = 0

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
        self.boton = ttk.Button(self.frame, text="Vista de LRU", cursor="hand2")

    def mngFrame(self, funcion):
        if funcion:
            # Pinto el frame
            self.frame.pack(expand=True, fill=tk.BOTH)
            self.boton.pack()
            self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

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
            self.tree = ttk.Treeview(self.frame, style="EstiloTabla.Treeview",columns=('#0','Referencia'))
            # Oculto la primera columna
            self.tree.heading('#0')
            self.tree.column('#0', width=0, stretch=tk.NO)
            # Creo las columnas
            self.tree.heading('#1', text='Referencia', anchor='center')
            self.tree.heading('#2', text='Página', anchor='center')
            self.tree.column('#1', width=80, anchor='center')
            self.tree.column('#2', width=80, anchor='center')
            self.tree.place(x=100, y=100, width=300, height=250)

            self.data = (
                ('Marco {}'.format(i), 'Proceso {}'.format(i))
                for i in range(1, self.memoria + 1)
            )
            
            for item in self.data:
                self.tree.insert('', 'end', values=(item[0], item[1]))
                
            # Añadir línea divisora entre columnas 1 y 2
            self.separator = ttk.Separator(self.frame, orient='vertical')
            self.separator.place(in_=self.tree, relx=1/2, rely=0, relheight=1)
            
        else:
            # Quito el frame
            self.frame.pack_forget()
