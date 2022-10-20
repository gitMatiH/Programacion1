'''
Introducir un arreglo de 10 elementos.
Eliminar la primera componente y mostrar el arreglo.
'''
#hay varias maneras de hacerlo
import random

#variante 1
lista = []
j = 10
for i in range(0,j):
    lista.append(random.randint(1, 100))
print("Lista de: ", len(lista),"elementos")
print("La lista en cuestión:")
print(lista)

lista.pop(0)
print(lista)
print()


#variante 2
lista = []
j = 10
for i in range(0,j):
    lista.append(random.randint(1, 100))
print("Lista de: ", len(lista),"elementos")
print("La lista en cuestión:")
print(lista)

elem = lista[0]

lista.remove(elem)
print(lista)
print()


#variante 3
lista = []
j = 10
for i in range(0,j):
    lista.append(random.randint(1, 100))
print("Lista de: ", len(lista),"elementos")
print("La lista en cuestión:")
print(lista)

del lista[0]
print(lista)
print()


#variante 4
lista = []
j = 10
for i in range(0,j):
    lista.append(random.randint(1, 100))
print("Lista de: ", len(lista),"elementos")
print("La lista en cuestión:")
print(lista)

lista_aux = lista[1:]
lista.clear()
lista = lista_aux
print(lista)
print()
