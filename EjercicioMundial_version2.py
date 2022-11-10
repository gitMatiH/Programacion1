#CODIGO POR JULIO CARDENAS


'''
Se quiere llevar una estadística de predicciones para el mundial, para
lo cual se consultan en dos sucursales de venta de electrodomésticos.
Boedo y Caballito
A los encuestados se les pregunta la edad y si Argentina resulta
campeón o subcampeón
Se carga información hasta que la edad ingresada sea 0.
Se debe cargar la información de la edad para cada sucursal.
Calcular la cantidad de encuestados en cada sucursal y determinar
cual sucursal tuvo mayor cantidad de encuestados.
Calcular la edad máxima de encuestados y determinar a qué sucursal
corresponde.
La sucursal se ingresa B para Boedo y C para caballito.
Ordenar el arreglo de mayor a menor.
Validar que la edad ingresada no sea menor a 0.
C para campeón y S para subcampeón
'''

# Declaración de funciones

def calcular_maximo(a):
    if len(a) > 0:
        maximo = a[0]
        for i in range(len(a)):
            if maximo < a[i]:
                maximo = a[i]    
        return maximo
    elif len(a) == 0:
        return -1

def calcular_porcentaje(len_suc,total):
    if total != 0:
        return (len_suc/total)*100
    elif total <=0:
        return -1

# Código principal

boedo = []
caballito = []

edad = int(input("Ingrese la edad"))

while edad != 0:
    while edad < 0:
       print("Por favor ingrese edad válida") 
       edad = int(input("Ingrese la edad"))
    suc = input("Ingrese la sucursal").upper()
    while suc != "B" and suc != "C":
        suc = input("Ingrese la sucursal").upper()

    if suc == "B":
        boedo.append(edad)
    else:
        caballito.append(edad)
    
    edad = int(input("Ingrese la edad"))
    

maximo_boedo = calcular_maximo(boedo)
maximo_caballito = calcular_maximo(caballito)

if maximo_boedo != -1:
    
    if maximo_boedo > maximo_caballito:
        print("Cantidad de edad máxima de encuestados en boedo",maximo_boedo)
    elif maximo_boedo < maximo_caballito:
        print("Cantidad máxima de encuestados en caballito",maximo_caballito)
    else:
        print("La cantidad de encuestados es la misma",maximo_boedo)
elif maximo_boedo == -1:
    print("ERROR")
    
# Calcular cantidad de encuestados totales
total = len(boedo) + len(caballito)
print("La cantidad de encuestados totales es:",total)    

# Calcular porcentaje encuestados Boedo
porcentaje = calcular_porcentaje(len(boedo),total)
if porcentaje != -1:
    print("El porcentaje es: ",porcentaje)
elif porcentaje == -1:
    print("ERROR")

# Ordenar
caballito.sort()
print(caballito)
