'''
numeros=[]
print (numeros)


numeros=[12,34,54]
print(numeros)

indice=int(input("ingese el indice del elemento del arrelo que quiere mostrar: "))
#while indice>2:
while not(indice<len(numeros)):
    print("error de indice")
    indice=int(input("ingese el indice del elemento del arrelo que quiere mostrar: "))

numero=numeros[indice]
print(numero)
'''

'''

print("ingrese nuevo arreglo")
elementos=int(input("ingrese cantidad de elementos: "))
i=0
array_elementos=[]
while i <= elementos-1:
    #procesar
    elemento=int(input("ingrese numero para añadir al arreglo: "))
    array_elementos.append(elemento)
    #actualizar
    i =i+1
print(array_elementos)

#imprimimos con un for los elementos en orden de ingreso
print("Longitud del array_elementos", len(array_elementos))
for j in range(0,len(array_elementos)):
    print("elemento de pos {}".format(j+1), array_elementos[j])

'''

## Ahora como función

def cargar_array(array, cantidad_elementos):
    i = 0
    while i < cantidad_elementos:
        elemento = int(input("Ingrese un elemento para agregar al array: "))
        array.append(elemento)
        i = i + 1

def imprimir_elementos(array):
    for i in range(0, len(array)):
        elemento = array[i]
        print("El elemento de la posición {} es: ".format(i+1) , elemento) 


array_elementos = []
n = int(input("Ingrese la cantidad de elementos a ingresar al array: "))
cargar_array(array_elementos, n)
print(array_elementos)

imprimir_elementos(array_elementos)

    
