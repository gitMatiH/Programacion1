from intercambiar import intercambiar as interc

def insertarEnOrden(indice_elemento, arreglo):
    #inserta en el orden correcto elemento último de un arreglo a su subarreglo ordenado
    while arreglo[indice_elemento-1]>arreglo[indice_elemento] and indice_elemento>0:
        #el i>0 es la condicion de corte si la primer condic de corte
        #no se realiza
        interc(indice_elemento, indice_elemento-1, arreglo)
        indice_elemento = indice_elemento-1


if __name__ == '__main__':

    arreglo = list(input("Ingrese arreglo: "))
    arreglo.sort()
    # prependear en el ingreso el analogo de 0x<num>
    arreglo.append(input("Número a insertar: "))
    print(arreglo)
    insertarEnOrden(len(arreglo)-1, arreglo)
    print(arreglo)

