'''
9) Ingresar las temperaturas registradas a distintas horas de un día
en grados hasta que ésta sea 100. Mostrar la temperatura máxima y la
temperatura mínima.
'''

##temp = float(input("Ingrese temperatura: "))
##temp_max = temp
##temp_min = temp
##while temp != 100:
##    if temp_max <= temp:
##        temp_max = temp
##    elif temp_min >= temp:
##        temp_min = temp
##    temp = float(input("Ingrese temperatura: "))
##print("temperatura máxima: ", "{}°C".format(temp_max))
##print("temperatura mínima: ", "{}°C".format(temp_min))

## variacion
import random

temperaturas = []   # el subíndice+1 nos dice la hora
for i in range (0, 24):
    temperatura = random.randint(-99, 10)
    print(temperatura)
    temperaturas.append(temperatura)
print(temperaturas)

i = 0
temp_max = temperaturas[0]
temp_min = temperaturas[0]
while i in range(0, 23):
    if temp_max <= temperaturas[i]:
        temp_max = temperaturas[i]
    elif temp_min >= temperaturas[i]:
        temp_min = temperaturas[i]
    i=i+1
print("el rango de temperaturas va desde", temp_min, "hasta", temp_max)
print("el rango es: mayor temperatura - menor temperatura =", temp_max - temp_min)

i=0
for i in range (0, len(temperaturas)):
    print("hora {}: {}°C".format(i, temperaturas[i]))
    i = i+1
