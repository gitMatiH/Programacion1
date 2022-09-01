'''
Ingresar el valor de la ganancia anual de una empresa y calcular su retención según
se encuentre dentro de los siguientes parámetros:

    Ganancia            |   Retención
    ______________________________________________________
    <= 10000            |   Cero
    >10000 y <= 15000   |   2% sobre (ganancia -10000)
    > 150000            |   300+5% sobre (ganancia -15000)
'''

print("Calcula la retención en base a ganancias.")

ganancias = int(input ("ingrese sus ganancias anuales:\n"))
if ganancias <= 10000:
    print ("retencion = cero")
elif ganancias >10000 and ganancias <= 15000:   # con or estaría mal, podría pasar algo fuera de rango. Aunque el primero lo filtra (creo)
    retencion = 2 * ganancias / 100 #retencion = (ganancia-15000)*0.02
    print ("retencion total = ", retencion)
else:   #usa la condición que queda por descarte, en este caso ganancias > 150000
    retencion = 300 + 5 * ganancias / 100       # retencion = 300 + (ganancia -15000)*0.05
    print ("retencion total = ", retencion)
