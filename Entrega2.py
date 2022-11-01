'''
Cargar un arreglo con 10 numeros y luego
Hacer una función que reciba como parámetro:

    Arreglo
    Numero cualquiera ingresado por teclado

Y retorne la cantidad de veces que encontró ese numero 
 
USAR FUNCIONES
'''
#import random


def buscar_numero(num,arr):
    contador = 0
    i = 0
    while i<len(arr):
        if arr[i] == num:
            contador = contador + 1
        i = i + 1
    return contador


arreglo = []
#print(arreglo)
for i in range(0, 10):
    numero = int(input("Ingrese un número entero: "))
    arreglo.append(numero)
    #print(arreglo)
print(arreglo)



###para test random
##lista = []
##n = 10 #random.randint(10, 20)
##for i in range(0,n):
##    lista.append(random.randint(1, 100))
##print("Lista de: ", len(lista),"elementos")
##print("La lista en cuestión:")
##print(lista)
##
##arreglo = lista

numero = int(input("Ingrese un número entero: "))
num = buscar_numero(numero,arreglo)
print("El número {} apareció {} veces.".format(numero, num))
