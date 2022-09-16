##Ej2
'''
Diseñar un algoritmo que permita:
Calcular el promedio semanal de gastos en un mes, ingresando como datos:
- Semana número
- Gasto semanal
El proceso termina cuando semana número es =5
'''

from decimal import Decimal

sumatoria_mensual = 0
i=1
semana_nro = int(input("Ingrese nro de semana: "))
while semana_nro != 5:
    gasto_semanal = Decimal(input("ingrese gasto de semana {}: ".format(semana_nro)))
    sumatoria_mensual = sumatoria_mensual + gasto_semanal
    semana_nro = int(input("Ingrese nro de semana: "))
    i = i+1

# si son menos de cuatro i'es, falta el gasto de una semana
if i < 4:   # si son mas, no importa porque se promedia con el i (los gastos
            # semanales igual se calculan como la suma)
    raise Exception("no ingresó los gastos de todo el mes")
else:
    promedio = sumatoria_mensual/4
    print("Cantidad de ingresos por teclado: {}".format(i))
    print("Promedio mensual: ", promedio)
