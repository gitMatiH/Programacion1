
def bubbleSort(arreglo):
    # ordenamos sobre el mismo arreglo
    i = 0
    while i<len(arreglo):
        j=0
        while j<(len(arreglo)-1-i): #-1 porque tenemos j+1 abajo, y -i para no recorrer los que ya sabemos que están ordenados
            if arreglo[j]>arreglo[j+1]:
                intercambiar(j,j+1,arreglo)
            j = j+1
        i = i+1

def intercambiar(i,j,arreglo):
    if i>-1 and i<len(arreglo) and j>-1 and j<len(arreglo):
        aux = arreglo[i]
        arreglo[i] = arreglo[j]
        arreglo[j] = aux


arreglo = [5,10,2,12,20,3,1,4,-1]
print(arreglo)
bubbleSort(arreglo)
print(arreglo)
