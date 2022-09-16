'''
Se ingresa descripcion y gasto de los gastos mensuales de comercio.
El ingreso finaliza cuando se ingresa gasto 0.
a) Necesitamos encontrar: el total de gastos, el mayor gasto efectuado
y su descripcion, el menor gasto efectuado y su descripcion
El promedio de gastos efectuados en el mes.
b) Cuantos gastos ocurrieron que fueran igual al mayor gasto (Desafío)
'''
## ver una buena notacion estandar para funciones y variables;
## camelcase empeando en min o mayus? y _para variables
from decimal import Decimal

descripciones = []
gastos = []

def ingresarGasto(descripciones, gastos):
    descripcion = input("Ingrese descripción de gasto: ")
    gasto = Decimal(input("Ingrese monto de gasto: "))
    print(gasto)
    descripciones.append(descripcion)
    gastos.append(gasto)
    return descripciones, gastos
    
def SeguirIngresando():  # =None u otro valor indica opcionalidad
    #print("Quiere ingresar gastos? Y/N: ")
    seguir = input("Quiere ingresar gastos? Y/N: ")    #print solo imprime, no devuelve nada. Por eso el imput imprimía None en la salida
    while not(seguir == 'Y' or seguir == 'N'):
        print("Comando inválido.")
        seguir = input(print("Quiere ingresar gastos? Y/N: "))        
    if seguir == 'Y':
        return True
    elif seguir == 'F':
        return False

while  SeguirIngresando():  # por que imprime None?
    descripciones, gastos = ingresarGasto(descripciones, gastos)
libroCuentas = dict(zip(descripciones, gastos))
print(libroCuentas)

