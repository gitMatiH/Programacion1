
def media(arreglo):
    ## precondición arreglo ordenado asc
    n = len(arreglo)
    if n%2 != 0:
        media = arreglo[int(n/2)]
        return media
    if n%2 == 0:
        pos_izq = int(n/2)
        indice_izq = pos_izq-1
        pos_der = int(n/2)+1
        indice_der = pos_der-1
        prom = (arreglo[indice_izq]+arreglo[indice_der])/2
        return prom

## test
if __name__ == '__main__':
    lista = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    print(lista)
    lista.sort()
    print(lista)
    med = media(lista)
    print(med)

    print()

    lista = [100, 60, 70, 900, 200]
    print(lista)
    lista.sort()
    print(lista)
    med = media(lista)
    print(med)



