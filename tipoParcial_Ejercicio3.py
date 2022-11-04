'''
Ejercicio 3

Se quiere validar el registro a una maratón. Para ello se pide como
datos el nombre, la edad y el género.

El cupo máximo es de 30 participantes. Si son mayores a 35 años la
categoría es mayores; si no, menores.

Calcular el promedio de edades para los maratonistas femeninos.

Calcular la edad mínima de participantes masculinos.

Mostrar la cantidad de anotados de categoría mayor.

Mostrar cuántos participantes masculinos tienen la edad mínima.

Obtener los nombres de los participantes masculinos que tienen la
edad mínima.

Usar funciones
'''

def seguirIngresando():
    seguir = input("Quiere seguir ingresando? S/N: ")
    while seguir != 'S' and seguir != 'N':
        print("Ingreso inválido.")
        seguir = input("Quiere seguir ingresando? S/N: ")
    return seguir

def promedioEdadesFemenino(edades, generos):
    ##procesa
    contador = 0
    acumulador = 0
    promedio = 0
    for i in range(0, len(generos)):
        if generos[i] == 'F':
            contador = contador + 1
            acumulador = acumulador + edades[i]
    if contador !=0:
        promedio = acumulador/contador
    return promedio

def edadMinimaMasculino(edades, generos):
    ##procesa
    i = 0
    while i<len(generos) and generos[i] != 'M':
        i = i+1
    if i != len(generos):
        edad_min = edades[i]    ## ojo, tiene que ser el primero de los masculinos
        #opciones: recorro hasta que encuentro el primero, o opcion de variable booleana de false
        # cuando todavia no lo encontro, y true cuando lo encontro y ahí se habilita la condicion
        # para comparar
        for i in range(0, len(generos)):
            if edades[i]<edad_min and generos[i] == 'M':
                edad_min = edades[i]
    else:
        edad_min = -1
        return edad_min
    return edad_min

def cantidadMayores(categorias):
    ##procesa
    cant_mayores = 0
    for i in range(0, len(categorias)):
        if categorias[i] == 'Mayor':
            cant_mayores = cant_mayores + 1
    return cant_mayores

##def cantMasculinosMenorEdad(nombres, edades, generos):
##    ##procesa
##    cant = 0
##    nombres = []
##    # si encuentra uno menor resetea la lista
##    return nombres, cant

# simplemente reuso edadMinimaMasculino
def cantidadMasculinosMenorEdad(edades, generos):
    ##procesa
    minimo = edadMinimaMasculino(edades, generos)
    cant_menores = 0
    for i in range(0, len(generos)):
        if generos[i] == 'M' and edades[i] == minimo:
            cant_menores = cant_menores + 1
    return cant_menores


def nombresMasculinosMenorEdad(nombres, edades, generos):
    ##procesa
    minimo = edadMinimaMasculino(edades, generos)
    nombres_menores = []
    for i in range(0, len(nombres)):
        if edades[i] == minimo and generos[i] == 'M':
            nombres_menores.append(nombres[i])
    return nombres_menores

nombres=[]
edades=[]
generos=[]
categorias=[]

##entrada datos y actualizacion
seguir = seguirIngresando()
i = 0

while i < 30 and seguir == 'S':

    nombre = input("Ingrese el nombre del participante: ")
    nombres.append(nombre)
    edad = int(input("Ingrese la edad del participante: "))
    edades.append(edad)

    genero = input("Ingrese género M/F: ")
    while genero != 'M' and genero != 'F':
        print("Ingreso inválido.")
        genero = input("Ingrese género M/F: ")
    generos.append(genero)

    #categoría
    if edad > 35:
        categorias.append("Mayor")
        #categoria = "Mayor" #asi no me anda
    elif edad <= 35:
        categorias.append("Menor")
        #categoría = "Menor"
    
    
    ##entrada datos y actualizacion
    seguir = seguirIngresando()
    i = i+1

## aca van los calculos en base a datos (o desde una base de datos)

print(nombres)
print(edades)
print(generos)
print(categorias)

promedio_edades_femenino = promedioEdadesFemenino(edades, generos)
print("El promedio de edades femenino es: ", promedio_edades_femenino)

edad_minima_masculino = edadMinimaMasculino(edades, generos)
print("La edad mínima de los participantes masculinos es: ", edad_minima_masculino)

cant_mayores = cantidadMayores(categorias)
print("La cantidad de participantes de la categoría mayores es: ", cant_mayores)

cantidad_masculinos_menor_edad = cantidadMasculinosMenorEdad(edades, generos)
print("La cantidad de participantes masculinos que tienen la menor edad es de: ", cantidad_masculinos_menor_edad)

nombres_masculinos_menor_edad = nombresMasculinosMenorEdad(nombres, edades, generos)
print("Los nombres de los participantes masculinos de menor edad son:")
print(nombres_masculinos_menor_edad)
