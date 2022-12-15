from procedimientos_comunes.intercambiar import intercambiar
#estamos interpretando la lista como un arreglo
#si materializamos esta interpretación sería un "downcast"
#pero hasta que no hacemos eso es una "simulación" de arreglo mediante listas

def insertarOrden(indice_elemento, arreglo):
    #inserta en el orden correcto elemento último de un arreglo a su subarreglo ordenado
    while arreglo[indice_elemento-1]>arreglo[indice_elemento] and indice_elemento>0:
        #el i>0 es la condicion de corte si la primer condic de corte
        #no se realiza
        intercambiar(indice_elemento, indice_elemento-1, arreglo)
        indice_elemento = indice_elemento-1


## precondición insertionSort:
#
##
def insertionSort(arreglo):

## poscondición insertionSort:
#
##
    # para tener una cantidad mínima de elementos a comparar
    j = 1
    while j < len(arreglo):
        #inserta nuevo; asume que la subsecuencia de anteriores
        #respeta relacion de orden y es transitiva, de inicio a fin
        #"empieza" por caso base! ordenar dos elementos, primitiva
        i = j
        insertarOrden(i, arreglo)
        j = j+1
    return(arreglo)



if __name__ == '__main__':

    # prependear en el ingreso el analogo de 0x<num>
    arreglo = list(input("Ingrese arreglo: "))
    print(arreglo)
    insertionSort(arreglo)
    print(arreglo)
