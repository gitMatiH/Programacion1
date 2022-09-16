'''
Se ingresa descripcion y gasto de los gastos mensuales de comercio.
El ingreso finaliza cuando se ingresa gasto 0.
a) Necesitamos encontrar: el total de gastos, el mayor gasto efectuado
y su descripcion, el menor gasto efectuado y su descripcion
El promedio de gastos efectuados en el mes.
b) Cuantos gastos ocurrieron que fueran igual al mayor gasto (Desafío)
'''

from decimal import Decimal

descripciones = []
gastos = []

def IngresarGasto(descripciones, gastos):
    descripcion = input("Ingrese descripción de gasto: ")
    gasto = Decimal(input("Ingrese monto de gasto: "))
    descripciones.append(descripcion)
    gastos.append(gasto)
    return descripciones, gastos
    
def SeguirIngresando():
    seguir = input("Quiere ingresar gastos? Y/N: ")
    while not(seguir == 'Y' or seguir == 'N'):
        print("Comando inválido.")
        seguir = input("Quiere ingresar gastos? Y/N: ")        
    if seguir == 'Y':
        return True
    elif seguir == 'F':
        return False

while  SeguirIngresando() == True:  # ==True es redundante, es para legibilidad
    descripciones, gastos = IngresarGasto(descripciones, gastos)

### Opciones: Diccionario, Lista de Tuplas, Lista de Listas

##Diccionario (key:value)
#libro_cuentas = dict(zip(descripciones, gastos))
#print(libro_cuentas)

##Lista de tuplas
#libro_cuentas = list(zip(descripciones, gastos))
#print(libro_cuentas)

##Lista de listas (hay manera mas directa?)
libro_cuentas = []
for i in range(0, len(gastos)):
    libro_cuentas.append([descripciones[i],gastos[i]])
print(libro_cuentas)

###

## ahora procesamos sobre la estructura (de datos, ADT) libro_cuentas:
#precondición: libro_cuentas != None
mayor = libro_cuentas[0]
menor = libro_cuentas[0]
supera = -1
for i in range(0, len(libro_cuentas)):
    if libro_cuentas[i][1] >= mayor[1]:
        supera = supera +1
        mayor = libro_cuentas[i]    # tb podríamos implementar una lista de iguales actuales, que se reinicia cada vez que supera al mayor
    elif libro_cuentas[i][1] <= menor[1]:
        menor = libro_cuentas[i]
print("Mayor gasto:")
print(mayor)
print("Mayor actualizado", supera,"veces")
print("Menor gasto")
print(menor)
