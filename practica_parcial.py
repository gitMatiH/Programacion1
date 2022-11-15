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

def promedio_f(edades, generos):
    promedio = 0
    contador = 0
    acumulador = 0
    for i in range(0, len(generos)):
        if generos[i] == 'F':
            acumulador = acumulador + edades[i]
            contador = contador +1
    if contador != 0:
        promedio = acumulador/contador
    return promedio

'''
def minimo_edad_m(edades, generos, nombres):
    ## no pide nombres, pero lo hacemos para practicar
    
    i = 0
    pos_min = 0
    # vamos a recorrer la lista de géneros y vamos a buscar el primer masculino.
    # como puede pasar que no haya ningún masculino, ponemos la condición "i<len(generos)"
    while i<len(generos) and generos[i] != "M":
        i=i+1

    # vamos a enganchar el siguiente if con la condición de "i<len(generos)"
    # la cual nos dice si hubo o no hubo participantes masculinos, y en base a eso procesa o no
    if i<len(generos):
        #procesar
        edad_min = edades[i]   # inicializamos con el que cortó el while, que es el primer masculino que queríamos
        pos_min = i
        for j in range(i,len(generos)): #recorremos el resto del array
            if edades[j]<edad_min and generos[j] == 'M':
                edad_min = edades[j]
                pos_min = j
    else:
        edad_min = -1
        return edad_min, nombre
    nombre = nombres[pos_min]
    return edad_min, nombre
'''

def cant_edad_min_m(edades, generos, edad):
    contador = 0
    for i in range(0, len(edades)):
        if edades[i] == edad and generos[i] == 'M':
            contador = contador + 1
    return contador

def cant_edad_min_m_2(edades, generos):
    minimo = minimo_edad_m(edades, generos)
    contador = 0
    for i in range(0, len(edades)):
        if edades[i] == minimo and generos[i] == 'M':
            contador = contador + 1
    return contador

def nombres_edad_min_m(nombres, edades, generos, edad_min):
    nombres_min = []
    for i in range(0, len(nombres)):
        if edades[i] == edad_min and generos[i] == 'M':
            nombres_min.append(nombres[i])
    return nombres_min

def minimo_edad_m(edades, generos):
    ## no pide nombres, pero lo hacemos para practicar
    i = 0
    # vamos a recorrer la lista de géneros y vamos a buscar el primer masculino.
    # como puede pasar que no haya ningún masculino, ponemos la condición "i<len(generos)"
    while i<len(generos) and generos[i] != "M":
        i=i+1

    # vamos a enganchar el siguiente if con la condición de "i<len(generos)"
    # la cual nos dice si hubo o no hubo participantes masculinos, y en base a eso procesa o no
    if i<len(generos):
        #procesar
        edad_min = edades[i]   # inicializamos con el que cortó el while, que es el primer masculino que queríamos
        pos_min = i
        for j in range(i,len(generos)): #recorremos el resto del array
            if edades[j]<edad_min and generos[j] == 'M':
                edad_min = edades[j]
    else:
        edad_min = -1
        return edad_min
    return edad_min

edades = []
nombres = []
generos = []
categorias = []

edades = [12, 56, 12, 22]
nombres = ['Juli', 'Mariana', 'Cacho', 'Maria']
generos = ['M', 'F', 'M', 'F']
categorias = ['MEN', 'MAY', 'MAY', 'MEN']

'''
# condicion de corte, nuestro código para cortar es ingresar edad negativa
edad = int(input("ingrese la edad del participante: "))

while len(nombres) < 30 and edad >= 0:
    edades.append(edad)

    nombre = input("Ingrese el nombre: ")
    nombres.append(nombre)

    genero = input("Ingrese genero, 'M' para masculino y 'F' para femenino: ")
    while genero != 'M' and genero != 'F':
        print("ingreso inválido")
        genero = input("Ingrese genero, 'M' para masculino y 'F' para femenino: ")
    generos.append(genero)

    #categoría Mayor decimos 'MAY', Menor 'MEN'
    if edad > 35:
        categorias.append("MAY")
    elif edad <= 35:
        categorias.append("MEN")
        

    # condicion de corte, nuestro código para cortar es ingresar edad negativa
    edad = int(input("ingrese la edad del participante: "))
'''


print(edades)
print(nombres)
print(generos)
print(categorias)

prom = promedio_f(edades, generos)
print("El promedio de edades femenino es: ", prom)

edad_min = minimo_edad_m(edades, generos)
print("El participante masculino de menor edad tiene", edad_min, "años.")

# hay dos maneras de hacerlo
# método 1) llamar a la función minimo_edad_m afuera de nuestra función
edad_m = minimo_edad_m(edades, generos)
cantmin = cant_edad_min_m(edades, generos, edad_min)
print("La cantidad de veces que apareció la mínima edad de participantes masculinos: ", cantmin)

# método 2) llamar a la función minimo_edad_m dentro de la función que definimos
cantmin = cant_edad_min_m_2(edades, generos)
print("La cantidad de veces que apareció la mínima edad de participantes masculinos: ", cantmin)


edad_m = minimo_edad_m(edades, generos)
nombres_min = nombres_edad_min_m(nombres, edades, generos, edad_m)
print("Los nombres de los participantes con la edad mínima:")
print(nombres_min)
