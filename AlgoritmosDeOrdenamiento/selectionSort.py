def intercambiar(indice_a, indice_b, arreglo):
    # intercambia elementos según los índices indicados
    aux=arreglo[indice_a]
    arreglo[indice_a] = arreglo[indice_b]
    arreglo[indice_b] = aux

def selectionSort(arreglo):
    for j in range(0, len(arreglo)):
        i = j
        pos_menor = i
        menor = arreglo[i]
        #busca menor del subarreglo
        while i < len(arreglo):
            if arreglo[i] < menor:
                pos_menor = i
                menor = arreglo[i]
            i = i+1
        intercambiar(pos_menor,j,arreglo)
