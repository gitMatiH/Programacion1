'''
Dado un arreglo, imprimir el lugar que ocupa el mínimo.
Tener en cuenta que este valor puede estar repetido, en
ese caso imprimir todos los lugares donde aparece este valor.
'''
import random

lista = []
j = random.randint(5,25)
for i in range(0,j):
    lista.append(random.randint(0, 100))
print("Longitud de la lista generada y llenada en forma aleatoria: ", len(lista))
print("La lista en cuestión:")
print(lista)

minimo = lista[0]
pos_minimo = [1]
for i in range(1,len(lista)):
    if lista[i] < minimo:       #acá usamos el índice
        #pos_minimo = [i+1]... funcionara?
        #o lo que es lo mismo
        pos_minimo.clear()
        minimo = lista[i]
        pos_minimo.append(i+1)  #y acá, por ser posición, le sumamos 1
    elif lista[i] == minimo:
        pos_minimo.append(i+1)
print("el mínimo de la lista fue: ", minimo)
print("y se produjo en la(s) posición(es):")
for i in range(0,len(pos_minimo)):
    print(pos_minimo[i])
