from procedimientos_comunes.intercambiar import intercambiar

def buscarIndiceMinimoSubarreglo(arreglo, inicio_subarreglo):
    i = inicio_subarreglo
    indice_minimo = inicio_subarreglo
    while i < len(arreglo):
        if arreglo[i] < arreglo[indice_minimo]:
            intercambiar(i, indice_minimo, arreglo)
        i = i+1

    return indice_minimo

## precondición selectionSort:
#
##
def selectionSort(arreglo):

## poscondición selectionSort:
#
##
    j = 0
    #acá la modularizacion es evidente desde el principio
    while j<len(arreglo):
        #caso base para buscar minimo es unario, sería un solo elemento es minimo por definicion
        #es el elemento comparado con el conjunto, y hay un solo elemento para comparar: el mismo 
        #para una relación de orden necesitas dos (uno si tenes en cuenta reflexividad pero no es a lo que apunto)
        indice_min = buscarIndiceMinimoSubarreglo(arreglo, j)   #aca el j en la funcion es el "desde"
        intercambiar(indice_min, j, arreglo)
        j = j+1



if __name__ == '__main__':

    # prependear en el ingreso el analogo de 0x<num>
    arreglo = list(input("Ingrese arreglo: "))
    print(arreglo)
    selectionSort(arreglo)
    print(arreglo)
