'''
Diseñar un algoritmo que permita:
3) Ingresar números hasta que el
último sea cero. Calcular la cantidad de positivos.
'''

contador = 0
num = int(input("Ingresar número: "))
while num != 0:
    if num > 0:
        contador = contador + 1
    num = int(input("Ingresar número: "))

print("Cantidad de positivos: ", contador)
