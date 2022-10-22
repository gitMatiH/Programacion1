'''
2) Se quieren calcular las ventas diarias de tres productos:

- alfajor triple $95.50
- conito de dulce de leche $110.00
- galletitas de coco $124.90


Se cargan los tickets de compra, la carga termina cuando se
ingresa 0 en el número de ticket o cuando se alcanzan
los 20 tickets ingresados. 
Se considera que se compra un sólo tipo de producto por ticket.
Los tipos de productos se identifican con una letra mayúscula.

Se ingresa la siguiente información

- nro de ticket
- producto (A para alfajor, C para conito, G para galletitas) 
- cantidad

Se pide

- Calcular y mostrar el monto total vendido en el día.
- Calcular y mostrar el porcentaje de conitos vendidos en cantidad 
- Mostrar cuál producto se vendió más (en cantidad) 
- Si el total de una compra es superior a los $170, realizar un
descuento del 5% y mostrar el monto a cobrar. 
'''

precio_alfajorTriple = float(95.50)
precio_conitoDDL = float(110.0)
precio_galletitasCoco = float(124.90)

cantidad_tickets = 0

cant_alfajorTriple = 0
cant_conitoDDL = 0
cant_galletitasCoco = 0

monto_dia = 0
porcentaje_conitos = 0
mas_vendido = 0

## bloque de ingreso de datos
numero_ticket = int(input("Ingrese el número de ticket: "))
while numero_ticket < 0:
    numero_ticket = int(input("Ingrese el número de ticket: "))
if numero_ticket != 0:
    producto = input("Ingrese producto ('A', 'C' o 'G'): ")
    while not(producto == 'A' or producto == 'C' or producto == 'G'):
        producto = input("Ingrese producto ('A', 'C' o 'G'): ")
    cant_producto = int(input("Ingrese cantidad: "))
    while cant_producto < 0:
        cant_producto = int(input("Ingrese cantidad: "))
############


while numero_ticket != 0 and cantidad_tickets < 20:
    cantidad_tickets = cantidad_tickets + 1
    if producto == 'A':
        cant_alfajorTriple = cant_alfajorTriple + cant_producto
        ##ojo, acá había un error
        monto = cant_producto * precio_alfajorTriple
    elif producto == 'C':
        cant_conitoDDL = cant_conitoDDL + cant_producto
        monto = cant_producto * precio_conitoDDL
    elif producto == 'G':
        cant_galletitasCoco = cant_galletitasCoco + cant_producto
        monto = cant_producto * precio_galletitasCoco

    if monto > int(170):
        monto_con_descuento = monto - 5*(monto)/100
        print("precio con descuento: ", monto_con_descuento)
        monto_dia = monto_dia + monto_con_descuento
    else:
        monto_dia = monto_dia + monto

    ## bloque de ingreso de datos
    numero_ticket = int(input("Ingrese el número de ticket: "))
    while numero_ticket < 0:
        numero_ticket = int(input("Ingrese el número de ticket: "))
    if numero_ticket != 0:
        producto = input("Ingrese producto ('A', 'C' o 'G'): ")
        while not(producto == 'A' or producto == 'C' or producto == 'G'):
            producto = input("Ingrese producto ('A', 'C' o 'G'): ")
        cant_producto = int(input("Ingrese cantidad: "))
        while cant_producto < 0:
            cant_producto = int(input("Ingrese cantidad: "))
    ############

if cant_alfajorTriple > cant_conitoDDL and cant_alfajorTriple > cant_galletitasCoco:
    mas_vendido = "Alfajor Triple"
elif cant_conitoDDL > cant_alfajorTriple and cant_conitoDDL > cant_galletitasCoco:
    mas_vendido = "Conito de Dulce de Leche"
elif cant_galletitasCoco > cant_alfajorTriple and cant_galletitasCoco > cant_conitoDDL:
    mas_vendido = "Galletitas de Coco"

##porcentaje conitos
## cant_conitos                                              ---     x
## cant_alfajorTriple + cant_conitoDDL + cant_galletitasCoco ---    100
porcentaje_conitos = cant_conitoDDL*100/(cant_alfajorTriple + cant_conitoDDL + cant_galletitasCoco)

print("porcentaje de venta de conitos sobre el total: ", porcentaje_conitos)
print("El producto mas vendido: ", mas_vendido)
print("El monto total del día en pesos: ", monto_dia)
