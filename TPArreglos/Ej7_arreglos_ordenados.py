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

## esta version, que es bastante distinta a la otra alternativa del Ej7,
## aprovecha el hecho de que estén ordenadas ambas listas, para hacer una
## búsqueda mas rápida. Corta cuando una de las listas termina ya que, por
## la condición de orden, no es posible que se repita otro elemento siguiente
## en la lista que no se terminó todavía.
## ¿El algoritmo guarda repetidos o los desecha?

import random

#para test sin random
#lista_a = [32, 94, 75, 31, 65, 38, 7, 79, 42, 70, 11, 57]
lista_a = []
n = random.randint(10, 20)
for i in range(0,n):
    lista_a.append(random.randint(1, 100))
print("Lista de: ", len(lista_a),"elementos")
print("La lista en cuestión:")
lista_a.sort()
print(lista_a)

#para test sin random
#lista_b = [32, 94, 44, 33, 65, 38, 7, 79, 42, 70, 11, 57]
lista_b = []
m = random.randint(10, 20)
for j in range(0,m):
    lista_b.append(random.randint(1, 100))
print("Lista de: ", len(lista_b),"elementos")
print("La lista en cuestión:")
lista_b.sort()
print(lista_b)

interseccion = []

i = 0
j = 0
while i!=len(lista_a) and j!=len(lista_b):
    if lista_a[i] < lista_b[j]:
        i = i+1
    else:
        if lista_a[i] > lista_b[j]:
            j = j+1
        else:   # son iguales
            interseccion.append(lista_a[i]) #también lo podríamos haber hecho con lista_b[i] 
            i = i+1
            j = j+1

print(interseccion)
        
