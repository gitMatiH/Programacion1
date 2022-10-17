'''
Dados dos arreglo s A y B de N<15 elementos cada uno,
calcular un arreglo C tal que C = A + B.
'''
import random 

##lista1 = []
##for i in range(0,15):
##    lista1.append(random.randint(0, 100))
##print("lista1")
##print(lista1)
##print("Longitud de lista1: ", len(lista1))
##
##lista2 = []
##for i in range(0,15):
##    lista2.append(random.randint(0, 100))
##print("lista2")
##print(lista2)
##print("Longitud de lista2: ", len(lista2))
##
##lista3 = []
##
##i = 0
##while i<len(lista2):
##    lista3.append(lista1[i]+lista2[i])
##    #print(lista3[i])
##    i = i + 1
##print("Lista de la suma miembro a miembro entre lista1 y lista2:")
##print(lista3)
##print()

'''
Todo lo que sigue estoy pensandolo en voz alta no darle bola
'''

print("El ejercicio interpretado como concatenación de listas:")
lista1 = []
for i in range(0,15):
    lista1.append(random.randint(0, 100))
print("lista1")
print(lista1)
print("Longitud de lista1: ", len(lista1))

lista2 = []
for i in range(0,15):
    lista2.append(random.randint(0, 100))
print("lista2")
print(lista2)
print("Longitud de lista2: ", len(lista2))
print()
print()

#variante 1 con método de operación entre listas
print("variante 1")
lista3 = []
print(lista3)
lista3 = lista1 + lista2    # ojo que lista3 no es una lista, es una referencia al resultado de la suma de las listas
print("asi quedo lista1:\n", lista1)
print("asi quedo lista2:\n", lista2)
print("asi quedo lista3:\n", lista3)
print(type(lista3))
print("del(lista1[15:])")
del(lista3[15:])
print("asi quedo lista3, debería ser igual a lista1 porque le sacamos todos los elementos que eran de lista2:\n", lista3)
print()
print()

print("mostrando que esta operacion es solo una referencia con listas, y que no se construye la lista3:")
lista3 = lista1
lista3.append('a')
print(lista3)
#usando el constructor:
lista3 = list(lista1)
print(type(lista3))
print()
print()

#variante 2 iterando sobre la segunda lista con for
print("variante 2")
lista3 = []
print("lista3:\n", lista3)
print("lista1:\n", lista1)
lista3 = lista1.copy()      # porque o sino si hago lista3 = lista1 se copia una referencia a lista1 y hace cualquier cosa (probar)
print("lista1:\n", lista1)
print("asi quedo lista3:\n", lista3)
for i in range(0, len(lista2)):     #también se puede escribir esta línea como "for i in range(0, len(lista2)):"
    lista3.append(lista2[i])
print("asi quedo lista1:\n", lista1)
print("asi quedo lista2:\n", lista2)
print("asi quedo lista3:\n", lista3)
print()
print()

#variante 3 iterando sobre la segunda lista con while
print("variante 3")
lista3 = [] #[] es un constructor de listas??
print("lista3:\n", lista3)
lista3 = list(lista1)       # uso el constructor de lista así se crea!! una lista igual a lista1, y no es solo una referencia a lista1
print("asi quedo lista3:\n", lista3)
i = 0
while i < len(lista2): 
    lista3.append(lista2[i])
    i = i + 1
print("asi quedo lista1:\n", lista1)
print("asi quedo lista2:\n", lista2)
print("asi quedo lista3:\n", lista3)
