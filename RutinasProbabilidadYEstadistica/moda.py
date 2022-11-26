
def intercambiar(i, j, lista):
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux

def insertionSortDosArrays(arreglo1, arreglo2):
    # usa el parámetro del primer array para ordenar
    i = 1    # así empezamos con un subarreglo de dos elementos para comparar
    while i < len(arreglo1):
        j = i
        #inserta nuevo elemento en el subarreglo de longitud j
        while j != 0 and arreglo1[j] > arreglo1[j-1]:
            intercambiar(j,j-1,arreglo1)
            intercambiar(j,j-1,arreglo2)
            j = j-1
        i = i+1

def insertar_ordenado(lista1, lista2):
    # ordena ambas listas con criterio descendiente (Mayor a menor) segun los indices de la primera
    # las listas están ligadas por los índices
    j = len(lista1)-1
    # en el while lo inserta
    while j >= 1 and lista1[j-1] < lista1[j]:
        intercambiar(j, j-1, lista1)
        intercambiar(j, j-1, lista2)
        j = j-1
    # sale del while ordenado

def moda(lista_dada):

    lista_numeros = []
    lista_apariciones = []
    # si el numero está en la lista_numeros, suma uno a su lista apariciones
    # sino
    # cada vez que encuentre un número nuevo, lo agrega en orden
    # a la lista_numeros con un "insertion" (flipea hasta que el j-1 sea mayor)
    # e inicializa en cero la misma posicion del arreglo lista_apariciones

    # procear lista dada
    for indice in range(0, len(lista_dada)):
        # busca si está
        i = 0
        while i < len(lista_numeros) and lista_dada[indice] != lista_numeros[i]:
            i = i+1
        if i < len(lista_numeros):
            # encontrado
            lista_apariciones[i] = lista_apariciones[i] +1
        elif i == len(lista_numeros):
            # no estaba en la lista
            lista_numeros.append(lista_dada[indice])
            lista_apariciones.append(1)
            insertar_ordenado(lista_numeros, lista_apariciones)
    print("lista de numeros que aparecieron, de mayor a menor")
    print(lista_numeros)
    print("lista de veces que apareció el número de la misma posicion de la lista anterior")
    print(lista_apariciones)
    
    # reordena por lista_apariciones de mayor a menor y devuelve el q mas aparecio
    ''' error
    #uso la funcion al reves -> no anduvo porque claro, no lo inserta en un arreglo ordenado
    ordenar_listas(lista_apariciones, lista_numeros)
    '''
    insertionSortDosArrays(lista_apariciones, lista_numeros)    

    print()
    
    print("lista de números que aparecieron")
    print(lista_numeros)
    print("cantidad de veces que aparecieron, de mayor a menor frecuencia")
    print(lista_apariciones)

    return lista_numeros[0], lista_apariciones[0]


if __name__ == '__main__':

    lista = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    
    numero_moda, cant_veces = moda(lista)
    print("la moda es", numero_moda, "con", cant_veces, "apariciones")
