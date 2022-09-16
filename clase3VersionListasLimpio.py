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
libro_cuentas = dict(zip(descripciones, gastos))
print(libro_cuentas)

