'''
Ingresar un arreglo de 10 componentes:
a. Imprimir la cuarta componente.
b. Imprimir las componentes en orden invertida.
c. Imprimir el producto entre la primera y la última componente.
d. Imprimir las componentes de índice impar.
e. Imprimir la suma de las componentes de índice par.
f. Imprimir la multiplicación de las componentes de índice impar.
g. Imprimir el arreglo que resulta de intercambiar la primera con la última
componente
'''


arreglo = [3, 5, 6, 8, 1, 3, 10, 4, 7, 80]
#print(arreglo[2])

# a
#print(arreglo[3])

### b
##indice = len(arreglo)-1
##while indice >= 0:
##    print(arreglo[indice])
##    indice = indice-1

#d
##ind_impar = 1
##while ind_impar <= len(arreglo)-1:
##    print(arreglo[ind_impar])
##    ind_impar = ind_impar + 2


k = 0
ind_impar = 2*k+1

while ind_impar <= len(arreglo)-1:
    print(arreglo[ind_impar])
    k = k+1
    ind_impar = 2*k+1
