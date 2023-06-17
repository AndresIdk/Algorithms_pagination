from view.index import Home # Modulo de la vista de inicio
from view.fifo import FifoFrame # Modulo de la vista de fifo
from view.lru import LruFrame # Modulo de la vista de lru

def changeStatusFIFO(estado, estadoAnterior):
    estadoAnterior.set(estado.get())
    estado.set(1)

def changeStatusLRU(estado, estadoAnterior):
    if estadoAnterior !=2: estadoAnterior.set(estado.get())
    estado.set(2)

def showInterfaces(estado, estadoAnterior, frames):
 
    if estado.get() == 1:
        # Mostrar vista del algoritmo FIFO
        if estadoAnterior.get() == 1:
            frames[0].mngFrame(0)
            frames[1].mngFrame(0)
            frames[2].mngFrame(0)
            frames[1].mngFrame(1)
        else:
            frames[0].mngFrame(0)
            frames[2].mngFrame(0)
            frames[1].mngFrame(1)
    else:
        # # Mostrar vista del algoritmo LRU
        if estadoAnterior.get() == 2:
            frames[0].mngFrame(0)
            frames[1].mngFrame(0)
            frames[2].mngFrame(0)
            frames[2].mngFrame(1)
        else:
            frames[0].mngFrame(0)
            frames[1].mngFrame(0)
            frames[2].mngFrame(1)

