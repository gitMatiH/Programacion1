'''
8) Ingresar las edades de 50 empleados de una empresa.
Determinar cuál es el rango de edades y mostrarlo.
'''

import random

edades_empleados = []
for i in range (0, 50):
    edad = random.randint(18, 99)
    print(edad)
    edades_empleados.append(edad)

print(edades_empleados)


mayor_edad = edades_empleados[0]
menor_edad = edades_empleados[0]
for i in range(0, len(edades_empleados)):
    if edades_empleados[i] >= mayor_edad:
        mayor_edad = edades_empleados[i]
    elif edades_empleados[i] <= menor_edad:
        menor_edad = edades_empleados[i]
print("el rango de edades va desde", menor_edad, "hasta", mayor_edad)
print("el rango es mayor_edad - menor edad =", mayor_edad - menor_edad)
