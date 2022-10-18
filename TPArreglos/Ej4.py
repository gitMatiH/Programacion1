'''
Dado un arreglo, imprimir los valores máximo y mínimo.
'''
import random

lista = []
j = random.randint(5,25)
for i in range(0,j):
    lista.append(random.randint(0, 100))
print("Longitud de la lista generada y llenada en forma aleatoria: ", len(lista))
print("La lista en cuestión:")
print(lista)

maximo = lista[0]
minimo = lista[0]
for i in range(1,len(lista)):
    if lista[i] > maximo:
        maximo = lista[i]
    if lista[i] < minimo:
        minimo = lista[i]
print("el máximo de la lista fue: ", maximo)
print("el mínimo de la lista fue: ", minimo)
