from procedimientos_comunes.intercambiar import intercambiar
#estamos interpretando la lista como un arreglo
#si materializamos esta interpretación sería un "downcast"
#pero hasta que no hacemos eso es una "simulación" de arreglo mediante listas

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
        #inserta
        while arreglo[i-1]>arreglo[i] and i>0:
            #el i>0 es la condicion de corte si la primer condic de corte
            #no se realiza
            intercambiar(i, i-1, arreglo)
            i = i-1
        j = j+1
    return(arreglo)



if __name__ == '__main__':

    # prependear en el ingreso el analogo de 0x<num>
    arreglo = list(input("Ingrese arreglo: "))
    print(arreglo)
    insertionSort(arreglo)
    print(arreglo)
