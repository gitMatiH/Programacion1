'''
1) Se carga un lote de números enteros que pueden ser tanto
negativos como positivos. La carga finaliza cuando el número
ingresado sea múltiplo de 3.
Se pide:
- Mostrar la cantidad de valores positivos y pares ingresados
- Mostrar el valor máximo y mínimo ingresado
'''

cant_positivos = 0
cant_pares = 0

num = int(input("ingrese un número positivo o negativo: "))
while num == 0:
    num = int(input("ingrese un número positivo o negativo: "))

valor_max = num
valor_min = num

while num%3 != 0:
    if num > 0:
        cant_positivos = cant_positivos +1
    if num%2 == 0:
        cant_pares = cant_pares +1
    if num >= valor_max:
        valor_max = num
    if num <= valor_min:
        valor_min = num
    num = int(input("ingrese un número positivo o negativo: "))
    while num == 0:
        num = int(input("ingrese un número positivo o negativo: "))

if num > 0:
    cant_positivos = cant_positivos +1
if num >= valor_max:
    valor_max = num
if num <= valor_min:
    valor_min = num

print("cantidad de valores positivos: ", cant_positivos)
print("cantidad de pares: ", cant_pares)
print("Valor máximo: ", valor_max)
print("Valor mínimo: ", valor_min)

##
##otra manera sería meter todo adentro de la estructura con un for
##y hardcodear a cero la condicion inicial
##...o incluso con un while y preguntar adentro


