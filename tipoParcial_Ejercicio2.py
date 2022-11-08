'''
Ejercicio 2


Se quiere llevar el control de variables climáticas semanales de una ciudad, para lo cual
se cargan los valores de presión y temperatura.

- Cargar los valores de presión y temperatura en dos estructuras (arreglos) separados para
los 7 días de la semana. 

- Deben cargarse ambos valores para cada día

- Deben validarse los valores ingresados. La temperatura podrá oscilar entre -15 y 52 grados.
La presión no podrá ser menor a 0.

Se pide:

- Generar una función que calcule y retorne el día con temperatura máxima

- Generar una función que calcule y retorne el promedio de presión para dos
días pasados por parámetro.

- Generar una función que calcule el día que se presentó la menor presión y retornar
la temperatura que correspondió a ese día.  
'''

## definicion de funciones
def cargar_dia():
    dia = int(input("Ingrese el día de la semana, 1-Lun ... 7-Dom: "))
    indice_dia = dia -1
    return indice_dia

def cargar_temperatura(indice_dia, temperaturas_semana):
    temp = float(input("Ingrese la temperatura del día: "))
    while temp < -15 or temp > 52:
        print("Error, temperatura invalida.")
        temp = float(input("Ingrese la temperatura del día: "))    
    temperaturas_semana[indice_dia] = temp

def cargar_presion(indice_dia, presiones_semana):
    pres = float(input("Ingrese la presión del día: "))
    while pres < 0:
        print("Error, presión invalida.")
        pres = float(input("Ingrese la presión del día: "))
    presiones_semana[indice_dia] = pres



## def cargar_mas
def cargar_mas():
    rta = input("¿Desea cargar mas datos? S/N: ")
    while rta != 'S' and rta != 'N':
        print("Error")
        rta = input("¿Desea cargar mas datos? S/N: ")
    if rta == 'S':
        sal = True
    elif rta == 'N':
        sal = False
    return sal

indice_dia = 0
temperaturas_semana = []
presiones_semana = []
while indice_dia < 7:
    temperaturas_semana.append('')
    presiones_semana.append('')
    indice_dia+=1

print(temperaturas_semana)
print(presiones_semana)

rta = cargar_mas()
while rta == True:
    ## cargar tupla actual
    indice_dia = cargar_dia()
    cargar_temperatura(indice_dia, temperaturas_semana)
    cargar_presion(indice_dia, presiones_semana)    

    rta = cargar_mas()

print(temperaturas_semana)
print(presiones_semana)
