import tkinter as tk

def remove_frame():
    frame.pack_forget()

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="¡Este es un frame!")
label.pack()

button = tk.Button(root, text="Quitar Frame", command=remove_frame)
button.pack()

root.mainloop()

