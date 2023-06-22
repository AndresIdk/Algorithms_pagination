def FIFO(fifoFrame, proceso, indice, band):
    if indice == 0 and band == 0:
        fifoFrame.actual = [i for i in range(1, fifoFrame.memoria + 1)]

    lista_vieja = fifoFrame.actual.copy()

    # Para la lista nueva
    if(proceso in lista_vieja):
        lista_nueva = lista_vieja.copy()
    else:
        fifoFrame.actual[indice] = proceso
        lista_nueva = fifoFrame.actual

    fifoFrame.showTables(lista_vieja, lista_nueva)

    print("Lista vieja: ", lista_vieja)
    print("Lista nueva: ", lista_nueva)


def LRU(LruFrame, proceso, indice, band):
    if indice == 0 and band == 0:
        LruFrame.actual = [i for i in range(1, LruFrame.memoria + 1)]

    lista_vieja = LruFrame.actual.copy()

    if(proceso in lista_vieja):
        lista_nueva = lista_vieja.copy()
    else:
        LruFrame.actual[indice] = proceso
        lista_nueva = LruFrame.actual

    LruFrame.showTables(lista_vieja, lista_nueva)

    print("Lista vieja: ", lista_vieja)
    print("Lista nueva: ", lista_nueva)



