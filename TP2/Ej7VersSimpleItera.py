'''
Se ingresa descripcion y gasto de los gastos mensuales de comercio.
El ingreso finaliza cuando se ingresa gasto 0.
a) Necesitamos encontrar: el total de gastos, el mayor gasto efectuado
y su descripcion, el menor gasto efectuado y su descripcion
El promedio de gastos efectuados en el mes.
b) Cuantos gastos ocurrieron que fueran igual al mayor gasto (Desafío)
'''

opc = 0
num1 = 0
num2 = 0

def menu(opc, num1, num2):
    print("Menú principal\n"
          "1. Sumar\n"
          "2. Restar\n"
          "3. Multiplicar\n"
          "4. Dividir\n"
          "5. Salir")
    opc = int(input("Seleccione una opción: "))
    if opc in(1,2,3,4):
        num1 = int(input("Ingresar primer número: "))
        num2 = int(input("Ingresar segundo número: "))
    elif opc == 5:
        pass
    else:
        pass
    return opc, num1, num2

opc, num1, num2 = menu(opc, num1, num2)

while opc != 5:
    if opc == 1:
        res = num1 + num2
    elif opc == 2:
        res = num1 - num2
    elif opc == 3:
        res = num1*num2
    elif opc == 4:
        if num2 == 0:
            res = "Error"
        else:
            res = num1/num2
    elif opc == 5:
        break
    else:
        pass
    print("\nResultado: ", res,"\n")
    opc, num1, num2 = menu(opc, num1, num2)

print("Saliendo.")
