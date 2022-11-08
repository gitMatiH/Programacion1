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

def dia_max_temp(temperaturas_semana):
    dia = 0
    indice_dia = 0
    max_temp = temperaturas_semana[dia]
    for indice_dia in range(0, len(temperaturas_semana)):
        if temperaturas_semana[indice_dia]>max_temp:
            max_temp = temperaturas_semana[indice_dia]
            dia = indice_dia
    return dia, max_temp

def promedio_presion(indice_dia_a, indice_dia_b, presiones_semana):
    promedio = (presiones_semana[indice_dia_a] + presiones_semana[indice_dia_b])/2
    return promedio

def dia_menor_pres(temperaturas_semana, presiones_semana):
    menor = presiones_semana[0]
    indice_menor = 0
    for i in range(0, len(presiones_semana)):
        if presiones_semana[i]<menor:
            menor = presiones_semana[i]
            indice_menor = i
    return temperaturas_semana[indice_menor], indice_menor

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
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas_semana = [20,23,45,21,18,46,44]
presiones_semana = [456,251,555,645,256,785,123]
'''
while indice_dia < 7:
    temperaturas_semana.append(0)
    presiones_semana.append(1)
    indice_dia+=1
'''
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

indice_dia, temp = dia_max_temp(temperaturas_semana)
print("La temperatura máxima de la semana fue el día", indice_dia+1,"y llegó a ", temp,"grados celsius")

dia_a = int(input("Ingrese el primer dia para el promedio de presiones, 1-Lun ... 7-Dom: "))-1
dia_b = int(input("Ingrese el segundo dia para el promedio de presiones, 1-Lun ... 7-Dom: "))-1
promedio = promedio_presion(dia_a, dia_b, presiones_semana)
print("El promedio de presión entre el día", dias_semana[dia_a],"y el día", dias_semana[dia_b], "fue de:", promedio)

temp, dia = dia_menor_pres(temperaturas_semana, presiones_semana)
print("La temperatura del día de menor presión fue de:",temp,"grados celsius. Eso pasó el día", dias_semana[dia])

