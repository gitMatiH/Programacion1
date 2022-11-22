'''
Ingresar valores en un array.
Solicitar la cantidad de elementos a ingresar.
Luego ingresar la cantidad indicada por el usuario.
Escribir una función que reciba como parámetro el array
y dos posiciones. Si las posiciones son válidas intercambiar
los elementos.

Escribir una función que devuelva el promedio de los elementos
del array.
Escribir una función que devuelva todos los elementos menores
que el promedio del array.
'''

def intercambiar(datos, pos1, pos2):
    if (pos1>=0 and pos1<len(datos)) and (pos2>=0 and pos2<len(datos)):
        aux=datos[pos1]
        datos[pos1]=datos[pos2]
        datos[pos2]=aux
    else:
        print("No son posiciones válidas.")

def promedio(arreglo):
    promedio = 0
    acumulador = 0
    cantidad= len(arreglo)
    i=0
    while i < cantidad:
        #procesa
        acumulador = acumulador + arreglo[i]
        #actualiza cierta cosa
        i=i+1
    if i != 0:
        promedio = acumulador/i
    return promedio

def menoresAPromedio(promedio, arreglo):
    menores = []
    pos_menores = []
    i = 0
    for i in range(0, len(arreglo)):
        if arreglo[i]==promedio:
            pos_menores.append(i+1)
            menores.append(arreglo[i])
        elif arreglo[i]<promedio:
            menores = []
            pos_menores = []
            pos_menores.append(i+1)
            menores.append(arreglo[i])
    return pos_menores, menores

datos = []
cantidad = int(input("Cuantos elementos: "))
if cantidad>0:
    for i in range(0, cantidad):
        datos.append(int(input("Ingrese elemento: ")))

print(datos)
p1=int(input("indice primer num: "))
p2=int(input("indice segundo num: "))
intercambiar(datos, p1, p2)
print(datos)

prom = promedio(datos)
print("El promedio de los elementos del array es: ", prom)

pos_menores, menores = menoresAPromedio(prom, datos)
print("Los menores y sus posiciones")
print("menores:    ", menores)
print("posiciones: ", pos_menores)


'''
## Test

Cuantos elementos: 6
Ingrese elemento: 1
Ingrese elemento: 2
Ingrese elemento: 1
Ingrese elemento: 1
Ingrese elemento: 3
Ingrese elemento: 4
[1, 2, 1, 1, 3, 4]
indice primer num: 1
indice segundo num: 5
[1, 4, 1, 1, 3, 2]
El promedio de los elementos del array es:  2.0
Los menores y sus posiciones
menores:     [1, 2]
posiciones:  [4, 6]
'''
