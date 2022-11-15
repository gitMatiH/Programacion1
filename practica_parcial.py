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
    

edades = []
nombres = []
generos = []
categorias = []

edades = [12, 56, 45, 22]
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

edad_min, nombre = minimo_edad_m(edades, generos, nombres)
print("El participante masculino de menor edad es", nombre,"y tiene", edad_min, "años.")
