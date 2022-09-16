'''
Calcular el sueldo de una persona, conociendo la cantidad
de horas que trabaja en el mes y el valor de la hora.
'''

horas = int(input("ingrese cantidad de horas trabajadas en el mes:\n"))

valorhora = float(input("ingrese el valor de una hora de trabajo\n"))

sueldo = horas*valorhora    #autocastea a float, hace un uptype del int

print("sueldo:", sueldo)
