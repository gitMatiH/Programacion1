
def intercambiar(i, j, arreglo):
    aux = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = aux


if __name__ == '__main__':

    i = int(input("Ingrese primer índice: "))
    j = int(input("Ingrese segundo índice: "))
    # prependear en el ingreso el analogo de 0x<num>
    arreglo = list(input("Ingrese arreglo: "))
    print(arreglo)
    intercambiar(i, j, arreglo)
    print(arreglo)
