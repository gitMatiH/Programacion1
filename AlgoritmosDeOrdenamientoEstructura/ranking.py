'''
Se pide cargar en memoria un arreglo de N posiciones.
Se pide generar un programa que emita un ranking con
los 10 números más grandes.
'''
## EN CONSTRUCCION
## aca iria el bien resuelto
from procedimientos_comunes.intercambiar import intercambiar
import random

lista = []
j = random.randint(10,110)  # n posiciones entre 10 y 110 
for i in range(0,j):
    lista.append(random.randint(0, 100))
print("Longitud de la lista generada y llenada en forma aleatoria: ", len(lista))
print("La lista en cuestión:")
print(lista)
#lista = [38, 32, 4, 46, 39, 10, 72, 71, 33, 86, 76, 21, 94, 62, 90, 47, 93, 45, 90, 52, 46, 33, 5, 2, 24, 77]

ranking = []
longitud = 0
max_longitud = 10  # queremos un ranking de diez elem


i = 0
while i < len(lista):
    pos = len(ranking)-1
    elem = lista[i]
    if ranking[pos] < elem:
        ranking[pos] = elem
        while pos > 0 and ranking[pos-1] < ranking[pos]:
            #lista = intercambiar(j-1,j,lista) ¿por que esto no anda?
            aux = ranking[pos-1]
            ranking[pos-1] = ranking[pos]   #promociona
            ranking[pos] = aux
            pos = pos - 1
    i = i + 1
print(ranking)
