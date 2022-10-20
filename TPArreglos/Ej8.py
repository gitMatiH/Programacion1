'''
Dado un arreglo de n elementos, calcular e
imprimir el menor de los múltiplos de 5 y
el mayor de los múltiplos de 10.Determinar
la posición de cada uno de ellos.
'''

import random

lista = []
j = random.randint(10,25)
for i in range(0,j):
    lista.append(random.randint(1, 100))
print("Lista de: ", len(lista),"elementos")
print("La lista en cuestión:")
print(lista)

menor_multiplo_cinco = lista[0]
pos_menor_multiplo_cinco = 0
mayor_multiplo_diez = lista[0]
pos_mayor_multiplo_diez = 0

i = 0

primero_mult_cinco = True
primero_mult_diez = True

if lista[0]%5 == 0 and menor_multiplo_cinco%5 != 0:
    #reemplazar (número y posición) registrados
    primero_mult_cinco = False
if lista[0]%10 == 0 and mayor_multiplo_diez%10 != 0:
    #reemplazar (número y posición) registrados
    primero_mult_diez = False

while i < len(lista):
    if primero_mult_cinco == False:
        if lista[i]%5 == 0:
            menor_multiplo_cinco = lista[i]
            pos_menor_multiplo_cinco = i+1
            primero_mult_cinco == True
    elif lista[i]%5 == 0 and menor_multiplo_cinco > lista[i]:
        #reemplazar (número y posición) registrados
        menor_multiplo_cinco = lista[i]
        pos_menor_multiplo_cinco = i+1
        
    if primero_mult_diez == False:
        if lista[i]%10 == 0:
            mayor_multiplo_diez = lista[i]
            pos_mayor_multiplo_diez = i+1
            primero_mult_diez = True
    elif lista[i]%10 == 0 and mayor_multiplo_diez < lista[i]:
        #reemplazar (número y posición) registrados
        mayor_multiplo_diez = lista[i]
        pos_mayor_multiplo_diez = i+1
        
    i = i + 1


#if menor_multiplo_cinco%5 != 0:
if primero_mult_cinco == False:
    print("no hubo múltiplos de cinco")
else:
    print("menor multiplo de cinco: ",menor_multiplo_cinco, "se dio en la posición",pos_menor_multiplo_cinco)

#if mayor_multiplo_diez%10 != 0:
if primero_mult_diez == False:
    print("no hubo múltiplos de diez")
else:
    print("mayor multiplo de diez: ",mayor_multiplo_diez, "se dio en la posición",pos_mayor_multiplo_diez)
