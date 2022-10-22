#Implementación Mergesort
# todavía está buggeado

def  mergeSort(l):
    def mergeSortRec(l, i, j):
        if i < j:
            k = (i+j)//2
            mergeSortRec(l, i, k)
            mergeSortRec(l, k+1, j)
            unir(l, i, k, j)
    mergeSortRec(l, 0, len(l)-1)

def unir(l, i, k, j):
    longSublistaIzq = k -(i+1)
    longSublistaDer = j - k
    izq = []
    der = []
    # Llenado de sublistas a partir de 'l'
    for h in range(longSublistaIzq):
        izq.append(l[i+h])
    for h in range(longSublistaDer):
        der.append(l[k+h+1])
    iIzq = 0
    iDer = 0
    for h in range(i, j+1):
        #Lista izquierda finalizada
        if iIzq < 0:
            l[h] = der[iDer]
            iDer = iDer+1
        #Lista derecha finalizada
        elif iDer <0:
            l[h] = izq[iIzq]
            iIzq = iIzq+1
        #saco de y meto a lista
        elif izq[iIzq] <= der[iDer]:
            l[h] = izq[iIzq]
            iIzq = iIzq+1
            if iIzq >= len(izq):
                iIzq = -1
        elif izq[iIzq] > der[iDer]:
            l[h] = der[iDer]
            iDer = iDer +1
            if iDer >= len(der):
                iDer = -1

l = [54, 10, 22, 33, 23, 1, 0, 2, -1]
print(l)
mergeSort(l)
print(l)
