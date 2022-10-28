'''
Se quiere procesar un lote de números que pueden ser
enteros positivos o negativos.
Se piden números hasta que se ingrese un número positivo
divisible por 5
Se pide:
-Calcular el pordentaje de los números impares ingresados
y mostrar la leyenda: "Menos del 20% de los números son impares"
o "Se ingresaron más del 20% de impares"
-Determinar y mostrar cuántos números ingresados se encuentran
entre el -1 (inclusive) y 12 (inclusive).
'''

#Ejercicio 2

contador = 0
contador_impares = 0
contador_rango = 0

##Bloque de ingreso
num = int(input("Ingrese un número entero positivo o negativo: "))
while num == 0:
    print("Error")
    num = int(input("Ingrese un número entero positivo o negativo: "))
contador = contador + 1

while num%5 != 0:
    
    if num%2 != 0:
        contador_impares = contador_impares + 1
    
    if (int(-1) <= num and num <= int(12)):
        contador_rango = contador_rango + 1


    ##Bloque de ingreso
    num = int(input("Ingrese un número entero positivo o negativo: "))
    while num == 0:
        print("Error")
        num = int(input("Ingrese un número entero positivo o negativo: "))
    contador = contador + 1

#cálculo porcentaje
#
#   contador_impares    -   x
#       contador        -   100
# 
# => x = contador_impares*100/contador

if contador != 0:
    porcentaje = contador_impares*100/contador

if porcentaje < float(20):
    print("Menos del 20 por ciento de los números ingresados son impares.")
elif porcentaje > float(20):
    print("Se ingresaron más del 20 por ciento de impares.")

print(contador_rango, "números se encuentran entre el -1 y 12, considerando el -1 y el 12.")
