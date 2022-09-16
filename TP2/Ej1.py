'''
Diseñar un algoritmo que permita:
1) Ingresar números hasta un múltiplo de 3.
Mostrar el último número ingresado.
'''

num = int(input("Ingrese un número: "))
while num % 3 != 0:
    num = int(input("Ingrese un número: "))
print(num)
