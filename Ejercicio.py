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

def ingresarEdad():
    edad = int(input("Ingrese la edad del encuestado: "))
    while edad < 0:
        print("Edad inválida.")
        edad = int(input("Ingrese la edad del encuestado: "))
    return edad

def ingresarRta():
    rta = input("Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: ")
    while not(rta=='C' or rta=='S'):
        print("Ingreso inválido.")
        rta = input("Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: ")
    return rta

def ingresarSuc():
    suc = input("Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: ")
    while not(suc=='B' or suc=='C'):
        print("Ingreso inválido.")
        suc = input("Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: ")
    return suc

def cantEncuestados(sucursales):
    i = 0
    suc_boe = 0
    suc_cab = 0
    while i<len(sucursales):
        if sucursales[i] == 'B':
            suc_boe = suc_boe+1
        elif sucursales[i] == 'C':
            suc_cab = suc_cab+1
        i = i + 1
    return suc_boe, suc_cab

def edadMaxima(edades, sucursales):
    i = 0
    edad = edades[i]
    suc = sucursales[i]
    while i < len(edades):
        if edad < edades[i]:
            edad = edades[i]
            suc = sucursales[i]
        i = i + 1
    return edad, suc

def mayor(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    elif a==b:
        return "iguales"

def swap(indice_a, indice_b, arreglo):
    # intercambia elementos según los índices indicados
    aux=arreglo[indice_a]
    arreglo[indice_a] = arreglo[indice_b]
    arreglo[indice_b] = aux
    

def ordenarTupla(arreglo1, arreglo2, arreglo3):
    ## ordena el arreglo1 de menor a mayor, y asume que arreglo2 y 3 están conectados al 1 por el índice
    ## y los ordena de manera acorde a 1 
    for j in range(0, len(arreglo1)):
        i = j
        pos_menor = i
        menor = arreglo1[i]
        #busca menor del subarreglo
        while i < len(arreglo1):
            if arreglo1[i] < menor:
                pos_menor = i
                menor = arreglo1[i]
            i = i+1
        swap(pos_menor,j,arreglo1)
        swap(pos_menor,j,arreglo2)
        swap(pos_menor,j,arreglo3)

'''
#test hardcodeado
edades      =   [23, 45, 22, 12, 33, 45, 54]
respuestas  =   ['C','S','C','S','S','C','C']
sucursales  =   ['B','C','C','C','C','B','B']
'''

## comentar este bloque si se quiere usar el test
edades = []
respuestas = []
sucursales = []

edad = ingresarEdad()
while edad != 0:
    #carga "tupla"
    edades.append(edad)
    rta = ingresarRta()
    respuestas.append(rta)
    suc = ingresarSuc()
    sucursales.append(suc)

    edad = ingresarEdad()
## comentar este bloque si se quiere usar el test


if len(sucursales) !=0:
    suc_boe, suc_cab = cantEncuestados(sucursales)
    if suc_boe > suc_cab:
        print("La sucursal con mayor cantidad de encuestados fue Boedo.")
    elif suc_boe < suc_cab:
        print("La sucursal con mayor cantidad de encuestados fue Caballito.")
    elif suc_boe == suc_cab:
        print("Ambas sucursales tuvieron el mismo nro de encuestados.")

if len(edades) != 0:
    edad, suc = edadMaxima(edades, sucursales)
    print("La edad máxima de un encuestado fue de",edad)
    if suc == 'B':
        print("y se lo encuestó en la sucursal de Boedo")
    elif suc == 'C':
        print("y se lo encuestó en la sucursal de Caballito")

if len(edades) != 0:
    ordenarTupla(edades, respuestas, sucursales)
    print("Tupla ordenada: ")
    print("edades:",edades)
    print("respuestas:",respuestas)
    print("sucursales:",sucursales)

###############################################

'''
salida del programa para test interactivo:
############################################
Ingrese la edad del encuestado: 23
Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: C
Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: B
Ingrese la edad del encuestado: 45
Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: S
Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: C
Ingrese la edad del encuestado: 22
Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: C
Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: C
Ingrese la edad del encuestado: 12
Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: S
Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: C
Ingrese la edad del encuestado: 33
Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: S
Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: C
Ingrese la edad del encuestado: 45
Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: C
Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: B
Ingrese la edad del encuestado: 54
Ingrese la respuesta a la encuesta, C para Campeón y S para Subcampeón: C
Ingrese la sucursal donde fue encuestado, B para Boedo y C para Caballito: B
Ingrese la edad del encuestado: 0
La sucursal con mayor cantidad de encuestados fue Caballito.
La edad máxima de un encuestado fue de 54
y se lo encuestó en la sucursal de Boedo
Tupla ordenada: 
edades: [12, 22, 23, 33, 45, 45, 54]
respuestas: ['S', 'C', 'C', 'S', 'S', 'C', 'C']
sucursales: ['C', 'C', 'B', 'C', 'C', 'B', 'B']
###########################
'''
