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


def LRU(lruFrame, proceso, indice, band):
    if indice == 0 and band == 0:
        lruFrame.actual = [i for i in range(1, lruFrame.memoria + 1)]

    lista_vieja = lruFrame.actual.copy()

    # lruFrame.showTables(lista_vieja, lista_nueva)


    print("Lista vieja: ", lista_vieja)
    # print("Lista nueva: ", lista_nueva)



