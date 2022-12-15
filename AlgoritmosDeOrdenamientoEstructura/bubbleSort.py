from procedimientos_comunes.intercambiar import intercambiar

## precondición bubbleSort:
#
##
def bubbleSort(arreglo):

## poscondición bubbleSort:
#
##
    j = len(arreglo)-1
    #while "tenga sentido" hacer la operacion anidada, i.e.: haya dos elementos
    #j>0 <=> j>=1 en este caso, por tratarse de enteros
    while j>0:
        i = 0
        while i<j:
            if arreglo[i+1]<arreglo[i]:
                intercambiar(i, i+1, arreglo)
            i = i+1
        j = j-1
    return(arreglo)


if __name__ == '__main__':

    # prependear en el ingreso el analogo de 0x<num>
    arreglo = list(input("Ingrese arreglo: "))
    print(arreglo)
    bubbleSort(arreglo)
    print(arreglo)
