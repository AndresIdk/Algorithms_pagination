import tkinter as tk
from tkinter import ttk

# Crear ventana
ventana = tk.Tk()

# Crear frame con fondo
frame_con_fondo = tk.Frame(ventana, bg="blue")
frame_con_fondo.pack(fill="both", expand=True)

# Crear botón dentro del frame
boton = ttk.Button(frame_con_fondo, text="Botón")
boton.pack(pady=20, padx=50)

# Ejecutar ventana
ventana.mainloop()
