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


##k = 0
##ind_impar = 2*k+1
##
##while ind_impar <= len(arreglo)-1:
##    print(arreglo[ind_impar])
##    k = k+1
##    ind_impar = 2*k+1


# c
datos = [3, 5, 6, 8, 1, 3, 10, 4, 7, 80]
numeros = []

##i = 0
##while i<10:
##    dato = int(input("Ingrese un valor: "))
##    numeros.append(dato)
##    #i += 1
##    i = i + 1

'''
##bloque de input
sigue = input("Ingrese V para agregar datos, F para cortar: ")
while not(sigue=='V' or sigue=='F'):
    sigue = input("Ingrese V para agregar datos, F para cortar: ")
##
    
while sigue == 'V':
    dato = int(input("Ingrese un valor: "))
    numeros.append(dato)

    ##bloque de input
    sigue = input("Ingrese V para agregar datos, F para cortar: ")
    while not(sigue=='V' or sigue=='F'):
        sigue = input("Ingrese V para agregar datos, F para cortar: ")
    ##
    

indice = 0
while indice<len(numeros):
    print(numeros[indice])
    indice += 1

'''

'''
if 3<len(datos):
    print(datos[3])
producto = datos[0]*datos[len(datos)-1]
print("Producto", producto)
indice = 0
while indice<len(datos):
    if indice%2 != 0:
        print(datos[indice])
    #if datos[indice]%2 != 0:
    indice += 1
'''

##for i in range(0,5):
##    print(i)
##
##print('****************')
##
##for i in range(0,len(datos)):
##    print(i)
##
##print('****************')
##
##sumatoria = 0
##for i in range(0,len(datos)):
##    print(datos[i])
##    if i != len(datos)-1:
##        print('+')
##    sumatoria = sumatoria + datos[i]
##
##print('=')
##print(sumatoria)

## maximos minimos buscar a partir de dado, generar arrays en base a arrays etc

#e
##ind_par = 0
##sumatoria_pares = 0
##while ind_par <= len(arreglo)-1:
##    print(arreglo[ind_par])
##    sumatoria_pares = sumatoria_pares + arreglo[ind_par]
##    ind_par = ind_par + 2
##
##print(sumatoria_pares)

#variante e
i = 0
sumatoria_pares = 0
print(arreglo)
while i <= len(arreglo)-1:
    if i%2 == 0 or i == 0:
        print(arreglo[i])
        sumatoria_pares = sumatoria_pares + arreglo[i]
    i = i + 1

print('=')
print(sumatoria_pares)
