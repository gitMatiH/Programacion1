'''
11) Escribir un algoritmo que encuentre los dos primeros números perfectos.
Un número perfecto es un entero positivo, que es igual a la suma de todos
los enteros positivos (excluido el mismo) que son divisores del número.
El primer número perfecto es 6, ya que lo divisores
de 6 son 1, 2, 3 y 1 + 2 + 3 = 6.
'''

def EsPerfecto(num):
    divisores = []
    for i in range (1, num):
        if num % i == 0:
            divisores.append(i)
    suma = 0
    for i in range(0, len(divisores)):
        suma = suma + divisores[i]
    if suma == num:
        return True
    else:
        return False

####Version input maximo a testear
##max = int(input("ingrese numero maximo a testear si es perfecto: "))
##perfectos = []
##for i in range(1, max+1):
##    if EsPerfecto(i):
##        perfectos.append(i)
##print("Perfectos encontrados en el rango especificado (1,{}): ".format(max), perfectos)

i = 1
cant = 0
perfectos = []
while cant != 2:
    if EsPerfecto(i):
        perfectos.append(i)
        cant = cant + 1
    i += 1
print("Perfectos encontrados: {}".format(cant))
print("Lista: ", perfectos)
