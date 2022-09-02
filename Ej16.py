'''
Ingresar dos números y sin resolver la multiplicación mostrar
una leyenda según el producto sea negativo, positivo o cero.
'''
from decimal import Decimal

print("Ingrese dos números en formato ...xxx.xxx... o entero:\n")
num1 = Decimal(input("primer número: "))
num2 = Decimal(input("segundo número: "))

def signoProducto(num1, num2):
    #print(type(num1), type(num2))
    if num1 == 0 or num2 == 0:
        return "cero"
    elif (0 < num1 and 0 < num2) or (num1 < 0 and num2 < 0):
        return "positivo"
    elif(0 < num1 and num2 < 0) or (num1 < 0 and 0 < num2):
        return "negativo"
##    ## alternativa al elif
##    else:   #(por descarte)
##        return "negativo"

res = signoProducto(num1, num2)
print(res)
