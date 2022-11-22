def intercambiar(indice_a, indice_b, arreglo):
    # intercambia elementos según los índices indicados
    aux=arreglo[indice_a]
    arreglo[indice_a] = arreglo[indice_b]
    arreglo[indice_b] = aux

def insertionSort(arreglo):
    i = 1    # así empezamos con un subarreglo de dos elementos para comparar
    while i < len(arreglo):
        j = i
        #inserta nuevo elemento en el subarreglo de longitud j
        while j != 0 and arr[j] < arr[j-1]:
            intercambiar(j,j-1,arreglo)
            j = j-1
        i = i+1

'''
## Test
arr = [3,2,5,1,6,7]
print(arr)
insertionSort(arr)
print(arr)
'''
