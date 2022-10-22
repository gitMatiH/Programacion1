'''
Ejercicio 3) 
Desarrollar un algoritmo que brinde información sobre el consumo de 20 clientes selectos de una empresa telefónica.
Para ello se ingresa, por cada uno de los clientes:
 
• Nombre del Cliente
• Duración de la llamada en minutos.
• Tipo de abono: “A”, “B” o “C”.
Para calcular el importe de cada llamada, nos informan que el costo por minuto, de acuerdo
al tipo de abono, es el siguiente:
 
• Abono “A” => $20 el minuto.
• Abono “B” => Los primeros 5 minutos a $20 el minuto. $10,5 el minuto adicional.
• Abono “C” => $10 el minuto con un máximo de $100 (Ej: si habla 15 minutos, paga $100).
Al finalizar la carga, el algoritmo debe mostrar:
 
1. La recaudación total de la empresa.
2. La cantidad de clientes por cada tipo de abono.
3. El porcentaje de llamadas con duración superior a 5 minutos.
'''
###
### Poner un caso de prueba con una lista de los 20 para corroborrarlo a mano
###

contador_clientes = 0
contador_superaCincoMin = 0
monto = 0

costo_a = float(20)
costo_b_1 = float(20)
costo_b_2 = float(10.5)
costo_c = float(10)
costo_c_max = float(100)

recaudacion_total = 0

clientes_a = 0
clientes_b = 0
clientes_c = 0

## bloque de ingreso
nombre = input("Ingrese nombre del cliente: ")
minutos = int(input("Ingrese el tiempo de llamada en minutos: "))
abono = input("Ingrese el tipo de abono, 'A', 'B' o 'C': ")
while not (abono == 'A' or abono == 'B' or abono == 'C'):
    abono = input("Ingrese el tipo de abono, 'A', 'B' o 'C': ")
contador_clientes = contador_clientes + 1
##

while contador_clientes <= 20:

    if minutos > 5:
        contador_superaCincoMin = contador_superaCincoMin + 1
    
    ## procesa
    if abono == 'A':
        clientes_a = clientes_a + 1
        monto = minutos * costo_a
    elif abono == 'B':
        clientes_b = clientes_b + 1
        if minutos <= 5:
            monto = minutos * costo_b_1
        else:
            monto = 5*costo_b_1 + (minutos-5)*costo_b_2
    elif abono == 'C':
        clientes_c = clientes_c + 1
        monto = minutos * costo_c
        if monto > 100:
            monto = costo_c_max

    recaudacion_total = recaudacion_total + monto
    
    ## bloque de ingreso
    nombre = input("Ingrese nombre del cliente: ")
    minutos = int(input("Ingrese el tiempo de llamada en minutos: "))
    abono = input("Ingrese el tipo de abono, 'A', 'B' o 'C': ")
    while not (abono == 'A' or abono == 'B' or abono == 'C'):
        abono = input("Ingrese el tipo de abono, 'A', 'B' o 'C': ")
    contador_clientes = contador_clientes + 1
    ##

print("Recaudacion total: ", recaudacion_total)
print("Cantidad de clientes de abono tipo 'A': ", clientes_a)
print("Cantidad de clientes de abono tipo 'B': ", clientes_b)
print("Cantidad de clientes de abono tipo 'C': ", clientes_c)

if contador_clientes != 0:
    porcentaje_superaCincoMin = contador_superaCincoMin*100/contador_clientes
    print("Porcentaje de llamadas con duración superior a 5 minutos: ", porcentaje_superaCincoMin)
