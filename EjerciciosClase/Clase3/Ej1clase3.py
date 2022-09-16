'''
Se ingresa descripcion y gasto de los gastos mensuales de comercio.
El ingreso finaliza cuando se ingresa gasto 0.
a) Necesitamos encontrar: el total de gastos, el mayor gasto efectuado
y su descripcion, el menor gasto efectuado y su descripcion
El promedio de gastos efectuados en el mes.
b) Cuantos gastos ocurrieron que fueran igual al mayor gasto (Desafío)
'''

from decimal import Decimal

## Toma input inicial
#gasto = float(input("Ingrese un gasto: "))     #usando float a veces las comparaciones me fallan
gasto = Decimal(input("Ingrese un gasto: "))    #por eso uso decimal
if gasto != 0:
    descripcion = input("Ingrese su descripción: ")

mayorGasto = gasto
mayorGastoDescripcion = descripcion
menorGasto = gasto
menorGastoDescripcion = descripcion
igualOMayor = -1    # Así cuando entra al primer if se pone en cero

while gasto != 0:
    ## Procesa
    if gasto >= mayorGasto:
        mayorGasto = gasto
        mayorGastoDescripcion = descripcion
        igualOMayor = igualOMayor + 1   # el primero no se cuenta, por eso el -1 de la línea 21
    elif gasto <= menorGasto:
        menorGasto = gasto
        menorGastoDescripcion = descripcion
    print("")
    ## Repite input
    gasto = int(input("Ingrese un gasto: "))
    if gasto != 0:
        descripcion = input("Ingrese su descripción: ")
#    else:      #opcional
#        break  #opcional

## Imprime resultados
print("")
print("El mayor gasto fue:")
print(mayorGasto, "; descripción:", mayorGastoDescripcion)
print("El menor gasto fue:")
print(menorGasto, "; descripción:", menorGastoDescripcion)
print("Cantidad de veces que el monto fue igual o mayor al mayor actual:", igualOMayor)
print("")
