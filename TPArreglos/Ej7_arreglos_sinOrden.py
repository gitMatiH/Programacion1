'''
Cargar dos arreglos de enteros de N y M posiciones.
Se pide generar un programa que produzca la intersección
entre los dos arreglos.
'''
#que sera mas rapido, ordenar la lista primero y comparar después
#o, si esta en interseccion, pasar y si no esta en interseccion,
#comparar cada elemento de la primer lista con
#todos los elementos de la segunda lista
#... o dará lo mismo?

import random

#para test sin random
#lista_a = [32, 94, 75, 31, 65, 38, 7, 79, 42, 70, 11, 57]
lista_a = []
n = random.randint(10, 20)
for i in range(0,n):
    lista_a.append(random.randint(1, 100))
print("Lista 'a' de: ", len(lista_a),"elementos")
print("La lista 'a' en cuestión:")
print(lista_a)
print()

#para test sin random
#lista_b = [32, 94, 44, 33, 65, 38, 7, 79, 42, 70, 11, 57]
lista_b = []
m = random.randint(10, 20)
for j in range(0,m):
    lista_b.append(random.randint(1, 100))
print("Lista 'b' de: ", len(lista_b),"elementos")
print("La lista 'b' en cuestión:")
print(lista_b)
print()

##interseccion = []
##
##i = 0
##j = 0

# podemos: ver cual lista es mas chica y comparar esa con los elementos de la mas grande,
# archivando los que ya aparecieron en una lista
# hacer version is in (que aprovecha un iterable) y version iteracion

##if elem_actual is not in lista_interseccion: #(elemActual es elemento (actual) de lista chica)
##    if elem_actual is in lista_b:
##        lista_interseccion.append(elem_actual)
##
### version iteración (con repeticion)
##i=0
##j=0
##while i < len(lista_a):
##    elem_actual = lista_a[i]
##    while j < len(lista_b):
##        j = j+1
##        if lista_a[i] == lista_b[j]:
##            lista_interseccion.append(elem_actual)
##    i = i+1
##
### version iteración (sin repeticion, version con un is not in)
##i=0
##j=0
##while i < len(lista_a):
##    elem_actual = lista_a[i]
##    while j < len(lista_b):
##        j = j+1
##        if lista_a[i] == lista_b[j] and elem_actual is not in lista_interseccion:
##            lista_interseccion.append(elem_actual)
##    i = i+1

# version iteración (sin repeticion, version con puras iteraciones)
i=0
j=0
lista_interseccion = []

while i < len(lista_a):
    elem_actual = lista_a[i]
    while j < len(lista_b):
        
        if lista_a[i] == lista_b[j]:
            k=0
            EsRepetido = False
            #for k in (0, len(lista_interseccion)): #alternativa for
            while k < len(lista_interseccion) and EsRepetido == False:  #alternativa while, esta mas buena porque corta si encuentra
                if elem_actual == lista_interseccion[k]:
                    EsRepetido = True
            if EsRepetido == False:
                lista_interseccion.append(elem_actual)
        #actualizo indice de lista_b
        j = j+1
    #actualizo indice de lista_a
    i = i+1

print("Lista de la intersección entre las listas a y b:\n", lista_interseccion)
        
