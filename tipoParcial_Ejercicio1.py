'''
Ejercicio 1

Ingresar por teclado un número entero mayor a cero: N

Luego crear un arreglo de tamaño N, a partir del ingreso de números enteros que sean
múltiplos de 3 pero no múltiplos de 5.

Generar una función que reciba como parámetro el arreglo y dos números enteros y realice
un swap de las posiciones de los arreglos.

Validar los números ingresados, en caso que ambos números sean iguales reemplazar
por un 0 en esas posiciones. 

Mostrar el arreglo con los cambios

Ejemplo:

arreglo = [5,-9,7,4,3,8]

numero 1 = 0

numero 2 = 3

arreglo = [4,-9,7,5,3,8]
'''

## interpreté que la función swap debe discernir si los números son válidos o no
## alternativamente, se podría escribir una función validar() y usarla para cada
## ingreso de los índices.

def swap(a, b, arr):
    if (a<0 or a>len(arr)) or (b<0 or b>len(arr)):
        return -1
    else:
        if arr[a] != arr[b]:
            aux = arr[a]
            arr[a] = arr[b]
            arr[b] = aux
        elif arr[a] == arr[b]:
            arr[a] = 0
            arr[b] = 0
        return 0


N = int(input("Ingrese el tamaño del arreglo a llenar: "))

i = 0
arreglo = []
while i < N:
    elemento = int(input("Ingrese un número entero múltiplo de tres pero no múltiplo de 5: "))
    if (elemento%3 != 0 or elemento%5 == 0):    # equivalente a not(notcond1 and notcond2) -> not(elemento%3 == 0 and elemento%5 != 0)
        print("Número inválido.")
        elemento = int(input("Ingrese un número entero múltiplo de tres pero no múltiplo de 5: "))
    arreglo.append(elemento)
    i = i +1

print(arreglo)

print("Ingrese dos índices: ")
indice_a = int(input("Indice a: "))
indice_b = int(input("Indice b: "))

sal = swap(indice_a, indice_b, arreglo)
if sal == 0:
    print("La operación fue exitosa.")
    print("El arreglo con cambios: ", arreglo)
elif sal == -1:
    print("Error, índices fuera de rango.")
