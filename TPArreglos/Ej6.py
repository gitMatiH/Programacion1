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
    #toma dos elementos de pos i y j de una lista y los intercambia
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    return lista

ranking = []    # queda en nosotros que la lista no se pase de los diez elementos
# si la lista es de solo diez elementos,
# van a quedar esos diez elementos en el ranking
# y van a estar ordenados de mayor a menor
while i < len(lista):
    # repasa el ranking de menor a mayor, o sea del ultimo al primero
    # y desplaza si es mayor, para y lo mete en la posicion actual
    # cuando el siguiente es mayor
    # para recorrer, vamos a usar j, j+1
    # para designar actual y proximo
    j = len(ranking)
    if j==0: #lista vacia, alternativo ranking == False
        ranking.append(lista[i])
    while j <= 0:
        if ranking[j-1] >= lista[i]:
            lista = intercambiar(j-1,j,lista)
        elif ranking[j-1] < lista[i]:
            pass
        j = j - 1
