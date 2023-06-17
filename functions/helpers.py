from view.index import Home # Modulo de la vista de inicio
from view.fifo import FifoFrame # Modulo de la vista de fifo
from view.lru import LruFrame # Modulo de la vista de lru

def changeStatusFIFO(estado, estadoAnterior):
    if estadoAnterior != 1: estadoAnterior.set(estado.get())
    estado.set(1)

def changeStatusLRU(estado, estadoAnterior):
    if estadoAnterior !=2: estadoAnterior.set(estado.get())
    estado.set(2)

def showInterfaces(ventana, estado, estadoAnterior):
    frames = [Home(ventana), FifoFrame(ventana), LruFrame(ventana)]

    if estado.get() == 0:
        print(estado.get())
        # Mostrar vista de inicio
        frames[estadoAnterior.get()].getFrame().pack_forget()
        frames[0].pack()
    elif estado.get() == 1:
        # Mostrar vista del algoritmo FIFO
        frames[estadoAnterior.get()].getFrame().pack_forget()
        frames[1].pack()
    else:
        # Mostrar vista del algoritmo LRU
        frames[estadoAnterior.get()].getFrame().pack_forget()
        frames[2].pack()
