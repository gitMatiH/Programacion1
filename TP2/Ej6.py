'''
6) Ingresar 10 números mayores a 3 y menores a 8.
Mostrar el valor ingresado en número y letras.
'''

contador = 0
print("Ingresar 10 números mayores a 3 y menores a 8")
num = int(input("Ingrese un número mayor a 3 y menor a 8: "))
for contador in range(0, 10):
    while not(3<num and num<8):
        print("Error")
        num = int(input("Ingrese un número mayor a 3 y menor a 8: "))
    res = ??
    num = int(input("Ingrese un número mayor a 3 y menor a 8: "))
