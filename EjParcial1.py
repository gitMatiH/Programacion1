'''
Ejercicio 1) 
Desarrollar un algoritmo que brinde información sobre las compras de una pizzería. 
Para ello se ingresa, por cada uno de los pedidos la siguiente información.


Número de pedido
Cantidad de pizzas grandes.
Tipo de pizza. "M" para muzzarella, "J" para jamón, "N" para napolitana.


La carga termina cuando en número de pedido se ingresa un -1 o se ingresaron 50 pedidos.


Los precios de las pizzas según la variedad son los siguientes:


Muzzarella => $1350.
Jamón => $1750
Napolitana => $1980


Sólo se compra un tipo de pizza por pedido.



Se pide:


1) El valor de ticket promedio en monto.
2) La cantidad de pizzas vendidas en total.
3) El porcentaje de pizzas de jamón sobre el total de los pedidos.
4) En el caso que la compra supere los 3.600 pesos se deberá calcular un descuento del 10% en el ticket.
Calcularlo y mostrar el monto a pagar. (Mostrar el total consumido en cada compra).
'''

precio_m = float(1350.0)
precio_j = float(1750.0)
precio_n = float(1980.0)

cant_pedidos = 0
cant_pizza_j = 0
pizzas_vendidas = 0
ventas_totales = 0


## bloque de ingreso de datos
num_pedido = int(input("Ingrese el número de pedido: "))
if num_pedido > 0:
    cant_pedidos = cant_pedidos + 1

    #valida por ingreso correcto
    cant_pizzasGdes = int(input("Ingresa la cantidad de pizzas grandes: "))
    while cant_pizzasGdes <= 0:
        cant_pizzasGdes = int(input("Ingresa la cantidad de pizzas grandes: "))

    #valida por ingreso correcto
    tipo_pizza = input("Ingrese tipo de pizza ('M', 'J' o 'N'): ")
    while not(tipo_pizza=='M' or tipo_pizza=='J' or tipo_pizza=='N'):
        tipo_pizza = input("Ingrese tipo de pizza ('M', 'J' o 'N'): ")
##

while num_pedido > 0 and cant_pedidos < 50:
    ##procesa
    pizzas_vendidas = pizzas_vendidas + cant_pizzasGdes
    if tipo_pizza == 'M':
        monto = precio_m * cant_pizzasGdes
    elif tipo_pizza == 'J':
        cant_pizza_j = cant_pizza_j + cant_pizzasGdes
        monto = precio_j * cant_pizzasGdes
    elif tipo_pizza == 'N':
        monto = precio_n * cant_pizzasGdes

    if monto > float(3600.0):
        #hacer descuento
        print("Total: ", monto)
        monto = monto - monto*10/100
        print("Monto con descuento: ", monto)

    print("Monto a pagar: ", monto)
    ventas_totales = ventas_totales + monto
    
    ## bloque de ingreso de datos
    num_pedido = int(input("Ingrese el número de pedido: "))
    if num_pedido > 0:
        cant_pedidos = cant_pedidos + 1

        #valida por ingreso correcto
        cant_pizzasGdes = int(input("Ingresa la cantidad de pizzas grandes: "))
        while cant_pizzasGdes <= 0:
            cant_pizzasGdes = int(input("Ingresa la cantidad de pizzas grandes: "))

        #valida por ingreso correcto
        tipo_pizza = input("Ingrese tipo de pizza ('M', 'J' o 'N'): ")
        while not(tipo_pizza=='M' or tipo_pizza=='J' or tipo_pizza=='N'):
            tipo_pizza = input("Ingrese tipo de pizza ('M', 'J' o 'N'): ")
    ##


## cálculos pedidos

if cant_pedidos != 0:
    monto_ticket_promedio = ventas_totales / cant_pedidos
    print("El monto promedio de un ticket es: ", monto_ticket_promedio)

print("Cantidad de pizzas vendidas: ", pizzas_vendidas)

if pizzas_vendidas != 0:
    porcentaje_jamon = cant_pizza_j * 100 / pizzas_vendidas
    print("Porcentaje de pizzas de jamón por sobre el total de pizzas vendidas: ", porcentaje_jamon,"%")
