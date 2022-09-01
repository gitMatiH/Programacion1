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
    print ("Retencion = cero")
elif 10000 < ganancias and ganancias <= 15000:
    retencion = (ganancias - 10000)*2/100
    print ("Retencion = ", retencion)
else:   #usa la condición que queda por descarte, en este caso ganancias > 150000
    retencion = 300 + (ganancias - 15000)*5/100
    print ("Retencion = ", retencion)
