'''
Ejercicio 5

El Ministerio de Salud le solicitó realizar un programa para llevar adelante
un censo de salud. Para ello se tomaron los siguientes datos:
peso, edad y sexo. 

Se realizan dos encuestas, y los datos fueron tomados en dos estaciones
ferroviarias:
Retiro y Constitución.


Cargar los datos de todas los encuestados. El ingreso concluye cuando
el encuestador ingresa un número menor a 0 en el peso. Todos los datos
deben ser validados.

Mostrar los datos cargados.

Determinar promediando cuál de las dos estaciones tiene las personas
con mayor peso (mayor promedio).

Ordenar los datos correspondiente al que se ingresaron más encuestas.
Mostrarlo.

Generar un nuevo arreglo con los pesos de ambos lotes que superen
el promedio general.
Mostrarlo.


'''

def calcular_promedio(arreglo):
    #necesito la cantidad de numeros promediados con 
    n=len(arreglo)
    #necesito la suma de los valores de los elementos del arreglo
    acumulador=0 
    for i in range(0,len(arreglo)):
        acumulador = acumulador + arreglo[i]
    if n!=0 :
        promedio=acumulador/n
        return promedio
    elif n==0:
        return -1

def promedio(pesos,estaciones,estacion):
    cantidad=0
    suma=0
    for i in range(0, len(estaciones)):
        if estaciones[i]==estacion:
            cantidad=cantidad+1
            suma=suma+pesos[i]
    if cantidad!=0:
        promedio=suma/cantidad
    return promedio

#bubbleSort(pesos,edades,sexos,estaciones)
def bubbleSort(arreglo1,arreglo2,arreglo3,arreglo4):
    # ordenamos por arreglo1 (peso)
    i = 0
    while i<len(arreglo1):
        j=0
        while j<(len(arreglo1)-1-i): #-1 porque tenemos j+1 abajo, y -i para no recorrer los que ya sabemos que están ordenados
            if arreglo1[j]>arreglo1[j+1]:
                intercambiar(j,j+1,arreglo1)
                intercambiar(j,j+1,arreglo2)
                intercambiar(j,j+1,arreglo3)
                intercambiar(j,j+1,arreglo4)
            j = j+1
    i = i+1

def intercambiar(i,j,arreglo):
    if i>-1 and i<len(arreglo) and j>-1 and j<len(arreglo):
        aux = arreglo[i]
        arreglo[i] = arreglo[j]
        arreglo[j] = aux


pesos=[]
edades=[]
sexos=[]
estaciones=[]

peso=int(input("Ingrese su peso: "))
while peso > 0:
    pesos.append(peso)

    edad=int(input("Ingrese su edad: "))
    while edad <= 0:
        print("Error, ingreso inválido.")
        edad=int(input("Ingrese su edad: "))
    edades.append(edad)
    
    sexo=input("ingrese su sexo, 'M' para masculino o 'F' para femenino: ")
    while sexo!='M' and sexo!='F':
        print("Ingreso inválido.")
        sexo=input("ingrese su sexo, 'M' para masculino o 'F' para femenino: ")
    sexos.append(sexo)

    estacion=input("Ingrese la estacion en donde se lo encuesto: R para retiro, C para Constitucion: ")
    while estacion!='R' and estacion!='C':
        print("Ingreso inválido.")
        estacion=input("Ingrese la estacion en donde se lo encuesto: R para retiro, C para Constitucion: ")
    estaciones.append(estacion)

    #lo necesitamos poner al final porque es nuestra condicion de corte
    peso=int(input("Ingrese su peso: "))

print("La lista de pesos es:", pesos)
print("La lista de edades es:",edades)
print("La lista de sexos es:",sexos)
print("La lista de estaciones es:",estaciones)
promedio_c = promedio(pesos, estaciones, "C")
promedio_r = promedio(pesos,estaciones, "R")
if (promedio_c > promedio_r):
    print("Constitución tiene mayor peso en promedio")
else:
    if promedio_r > promedio_c:
        print("Retiro tiene un mayor peso en promedio")
    else: 
        print("Ambos tienen el mismo promedio")


