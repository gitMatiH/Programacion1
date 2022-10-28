'''
Escribir las funciones necesarias para que el siguiente
código funcione:


valor1 = int(input())
valor2 = int(input())
operacion = input()
if operacion == "suma":
    print("Resultado", suma(valor1, valor2))
elif operacion == "resta":
    print("Resultado", resta(valor1, valor2))
'''

# definicion de funciones
def suma(num1, num2):
    res = num1 + num2
    return res

def resta(num1, num2):
    res = num1 - num2
    return res

#declaraciones
valor1 = int(input("Ingrese un número: "))
valor2 = int(input("Ingrese un número: "))
operacion = input("Ingrese una operación, 'suma'"
                  " para sumar y 'resta' para restar: ")

#codigo
if operacion == "suma":
    print("Resultado", suma(valor1, valor2))
elif operacion == "resta":
    print("Resultado", resta(valor1, valor2))
