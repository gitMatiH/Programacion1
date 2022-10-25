'''
Se quiere procesar un lote de números que pueden ser enteros positivos o
negativos. Se piden números hasta que se ingrese un número negativo múltiplo
de tres.

Se pide:
calcular el porcentaje de pares de los números ingresados
mostrar la leyenda:
"De los números, la mayoría son pares" en caso de superar el 50 por ciento o
"La minoría de los números no son pares"

Determinar y mostrar cuántos números ingresados se encuentran entre -4 y 20
(considerar el -4 y el 20)
'''
# inicializaciones para el porcentaje
cantidad_nums = 0
cantidad_nums_pares = 0
# inicializaciones para segunda parte enunciado
n = 0

# ingresos
numero = int(input('ingrese un número entero positivo o negativo: '))


# % devuelve el resto de la división entera y / devuelve el cociente
# // floor devuelve cuánto dió la división entera
while not(numero < 0 and numero%3 == 0):

    # procesa
    if numero%2 == 0:
        cantidad_nums_pares = cantidad_nums_pares + 1
    cantidad_nums = cantidad_nums + 1

    if numero >= -4 and numero <= 20:
        n = n+1
    # termina de procesar

    # ingresa datos
    numero = int(input('ingrese un número entero positivo o negativo: '))


porcentaje = (100 * cantidad_nums_pares)/cantidad_nums
# print("El porcentaje de números pares es: " , porcentaje)
if porcentaje > 50:
    print("De los números, la mayoría son pares")
else:
    print("La minoría de los números son pares")

if porcentaje > 50:
    print("La minoría de los números no son pares")

# segunda parte del enunciado

print("La cantidad de números entre el -4 y 20, inclusive, es: " , n)

    



    
 
