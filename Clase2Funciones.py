'''Ingresar valores en un array
Solicitar la cantidad de elementos a ingresar. 
Luego ingresar la cantidad indicada por el usuario.
Escribir una función que reciba como parámetro el array 
y dos posiciones. Si las posiciones son válidas intercambiar los elementos.

Escribir una función que devuelva el promedio de los elementos del array
Escribir una función que devuelva 
todos los elementos menores que el promedio del array.'''

def intercambiar(datos, pos1, pos2):
    if (pos1>=0 and pos1<len(datos)) and (pos2>=0 and pos2<len(datos)):
        auxiliar=datos[pos1]
        datos[pos1]=datos[pos2]
        datos[pos2]=auxiliar
    else:
        print("No son posiciones validas")    

datos=[]
cantidad=int(input("Cuantos elementos"))
if cantidad>0:
    for i in range(0, cantidad):
        datos.append(int(input("Ingrese elemento")))
print (datos)
p1=int(input("Primera posicion"))
p2=int(input("Segunda posicion"))
intercambiar(datos, p1,p2) 
print (datos)