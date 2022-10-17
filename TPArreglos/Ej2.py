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

'''
a. Imprimir la cuarta componente.
'''
print('a)')
print(arreglo)
print(arreglo[3])

print()

'''
b. Imprimir las componentes en orden invertida.
'''
print('b)')
print(arreglo)
indice = len(arreglo)-1
while indice >= 0:
    print(arreglo[indice])
    indice = indice-1

print()

'''
c. Imprimir el producto entre la primera y la última componente.
'''
print('c)')
print(arreglo)
producto = arreglo[0]*arreglo[len(arreglo)-1]
print(producto)

print()

'''
d. Imprimir las componentes de índice impar.
'''
#variante 1
print('d)')
print(arreglo)
ind_impar = 1
while ind_impar <= len(arreglo)-1:
    print(arreglo[ind_impar])
    ind_impar = ind_impar + 2

#variante 2
print()
k = 0
ind_impar = 2*k+1

while ind_impar <= len(arreglo)-1:
    print(arreglo[ind_impar])
    k = k+1
    ind_impar = 2*k+1

#variante 3
print()
indice = 1
while indice <= len(arreglo)-1:
    if indice%2!=0 or indice == 0:
        print(arreglo[indice])
    indice = indice + 1

print()

'''
e. Imprimir la suma de las componentes de índice par.
'''
print('e)')

i = 0
sumatoria_pares = 0     # neutro para la suma
print(arreglo)
while i <= len(arreglo)-1:
    if i%2 == 0 or i == 0:
        print(arreglo[i])
        if not(i+1 == len(arreglo)-1 or i+1 == len(arreglo)): #así no imprime el último +, se fija si está en el ultimo o anteultimo
            print('+')
        sumatoria_pares = sumatoria_pares + arreglo[i]
    i = i + 1

print('=')
print(sumatoria_pares)

print()

'''
f. Imprimir la multiplicación de las componentes de índice impar.
'''
print('f)')

i = 0
productoria_impares = 1     # neutro para el producto
print(arreglo)
while i <= len(arreglo)-1:
    if i%2 != 0:
        print(arreglo[i])
        if not(i+1 == len(arreglo)-1 or i+1 == len(arreglo)): #así no imprime el último *, se fija si está en el ultimo o anteultimo
            print('*')
        productoria_impares = productoria_impares * arreglo[i]
    i = i + 1

print('=')
print(productoria_impares)


'''
g. Imprimir el arreglo que resulta de intercambiar la primera con la última componente
'''
print('g')
print(arreglo)
aux = arreglo[0]
arreglo[0] = arreglo[len(arreglo)-1]
arreglo[len(arreglo)-1] = aux
print(arreglo)
            
