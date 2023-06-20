import tkinter as tk
from tkinter import ttk


class FifoFrame(ttk.Frame): 
    def __init__(self, parent):
        super().__init__(parent)

        self.memoria = 0
        self.actual = []
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

        # Añadir línea divisora entre columnas 1 y 2
        self.separator = ttk.Separator(self.frame, orient='vertical')
        
        # Creo la tabla de la data vieja
        self.tree_vieja = ttk.Treeview(self.frame, style="EstiloTabla.Treeview",columns=('#0','Referencia'))
        # Oculto la primera columna
        self.tree_vieja.heading('#0')
        self.tree_vieja.column('#0', width=0, stretch=tk.NO)
        # Creo las columnas
        self.tree_vieja.heading('#1', text='Referencia', anchor='center')
        self.tree_vieja.heading('#2', text='Página', anchor='center')
        self.tree_vieja.column('#1', width=80, anchor='center')
        self.tree_vieja.column('#2', width=80, anchor='center')

        # Creo la tabla de la data nueva
        self.tree_nueva = ttk.Treeview(self.frame, style="EstiloTabla.Treeview",columns=('#0','Referencia'))
        # Oculto la primera columna
        self.tree_nueva.heading('#0')
        self.tree_nueva.column('#0', width=0, stretch=tk.NO)
        # Creo las columnas
        self.tree_nueva.heading('#1', text='Referencia', anchor='center')
        self.tree_nueva.heading('#2', text='Página', anchor='center')
        self.tree_nueva.column('#1', width=80, anchor='center')
        self.tree_nueva.column('#2', width=80, anchor='center')



    def mngFrame(self, funcion):
        if funcion:
            # Pinto el frame
            self.frame.pack(expand=True, fill=tk.BOTH)
            self.boton.pack()
            self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
            self.tree.place(x=100, y=100, width=300, height=250)

            self.data = (
                ('Marco {}'.format(i), 'Proceso {}'.format(i))
                for i in range(1, self.memoria + 1)
            )
            
            for item in self.data:
                self.tree.insert('', 'end', values=(item[0], item[1]))
                
            self.separator.place(in_=self.tree, relx=1/2, rely=0, relheight=1)

        else:
            # Quito el frame
            self.frame.pack_forget()
        
    def showTables(self, lista_vieja, lista_nueva):
        self.tree.pack_forget()
        self.separator.pack_forget()

        self.data_vieja = (
                ('Marco {}'.format(i), 'Proceso {x}'.format(x=lista_vieja[i-1]))
                for i in range(1, self.memoria + 1)
        )

        for item in self.data_vieja:
                self.tree_vieja.insert('', 'end', values=(item[0], item[1]))

        self.tree_vieja.place(x=100, y=100, width=300, height=250)

        self.data_nueva = (
                ('Marco {}'.format(i), 'Proceso {x}'.format(x=lista_nueva[i-1]))
                for i in range(1, self.memoria + 1)
        )

        for item in self.data_nueva:
                self.tree_vieja.insert('', 'end', values=(item[0], item[1]))

        self.tree_nueva.place(x=500, y=100, width=300, height=250)


