'''
ingreso en un array 10 valores y tengo que generar/encontrar
el mayor elemento del array, pero sabiendo se puede repetir.
Quiero saber en qué posiciones se encuentra el mayor.
'''

# buggeado, no anda

numeros = [2,4,5,70,7,70,9,1,20,70]
print(numeros)

i = 0
mayor = numeros[i]
posiciones_mayor = []

def evaluar_mayor(numeros, i, mayor, posiciones_mayor):
    if numeros[i] > mayor:
        # actualiza el mayor
        mayor = numeros[i]
        # resetea la lista de apariciones del mayor
        posiciones_mayor = []
    if numeros[i] == mayor:
        # actualiza la lista de apariciones del mayor
        # el +1 es para pasar de ser indice a ser posicion
        pos = i + 1
        posiciones_mayor.append(pos)
    return (mayor, posiciones_mayor)

def buscar_mayor(numeros, i, mayor, posiciones_mayor):
# el while + la funcion evaluar_mayor() sería algo que podemos poner en la función buscar_mayor()
# buscar_mayor() = while + evaluar_mayor()
    while i < len(numeros):
        mayor, posiciones_mayor = evaluar_mayor(numeros, i, mayor, posiciones_mayor)
        i = i+1
        print("paso {}".format(i))
    return mayor, posiciones_mayor

print("El mayor es: ", mayor)
print("Y se apareció en las posiciones", posiciones_mayor)
    
