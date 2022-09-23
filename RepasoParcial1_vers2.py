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

primera_vuelta = True ## tb se puede hacer con contador
##primera_vuelta = 0
sigue = True

while sigue == True:
    num = int(input("ingrese un número positivo o negativo: "))
    while num == 0:
        num = int(input("ingrese un número positivo o negativo: "))

    if primera_vuelta == True:
        valor_max = num
        valor_min = num
        primera_vuelta = False
        ##primera_vuelta = primera_vuelta +1
        ##sirve mas si queremos trackear cuantas veces loopea

    if num > 0:
        cant_positivos = cant_positivos +1
    if num%2 == 0:
        cant_pares = cant_pares +1
    if num >= valor_max:
        valor_max = num
    if num <= valor_min:
        valor_min = num
    if num%3 == 0:
        sigue = False


    
print("cantidad de valores positivos: ", cant_positivos)
print("cantidad de pares: ", cant_pares)
print("Valor máximo: ", valor_max)
print("Valor mínimo: ", valor_min)
