'''
Se pide cargar en memoria un arreglo de N posiciones.
Se pide generar un programa que emita un ranking con
los 10 números más grandes.
'''
import random

lista = []
j = random.randint(10,110)  # n posiciones entre 10 y 110 
for i in range(0,j):
    lista.append(random.randint(0, 100))
print("Longitud de la lista generada y llenada en forma aleatoria: ", len(lista))
print("La lista en cuestión:")
print(lista)

def intercambiar(i,j,lista):
    #precondicion i<j
    #toma dos elementos de pos i y j de una lista y los intercambia
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux
    return lista

ranking = []
longitud = 10   # queremos un ranking de diez elem
aux = lista[0]
for i in range(0,longitud):
    ranking.append(aux)

while i < len(lista):
    j = len(ranking)-1
    elem = lista[i]
    while j > 0:
        if ranking[j-1] < ranking[j]:
            lista = intercambiar(j-1,j,lista)
        j = j - 1

print(ranking)
