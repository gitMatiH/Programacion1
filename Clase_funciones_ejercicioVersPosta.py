'''
Escribir las funciones necesarias para que el siguiente
código funcione:


valor1 = ingreso("Ingrese numero")
valor2 = ingreso("Ingrese numero")
operacion = ingreso("Ingrese operacion")
if operacion == "suma":
    print("Resultado", suma(valor1, valor2))
elif operacion == "resta":
    print("Resultado", resta(valor1, valor2))
'''

# definicion de funciones

##def ingreso(texto):
##    if texto == "Ingrese numero":
##        sal = int(input(texto))
##    elif texto == "Ingrese operacion":
##        texto = "Ingrese una operación, 'suma' para sumar y 'resta' para restar: "
##        sal = input(texto)
##    return sal


### Alternativa 1:
##def ingreso(texto):
##    x=input(texto)
##    if texto == "Ingrese numero":
##        x = int(x)
##    return x

##def ingreso(texto):
##    x=input(texto)
##    if texto == 'suma' or texto == 'resta':
##        x = int(x)
##    elif texto!= 'suma' and texto!= 'resta':
##        #nada
##        pass
##    return x
### como nunca hace el typecast, hace una concatenacion de strings

def ingreso(texto):
    x = input(texto)
    if x != 'suma' and x != 'resta':
        x = int(x)
    #else x == 'suma' or 
    return x

def suma(num1, num2):
    res = num1 + num2
    return res

def resta(num1, num2):
    res = num1 - num2
    return res

#declaraciones
valor1 = ingreso("Ingrese numero")
valor2 = ingreso("Ingrese numero")
operacion = ingreso("Ingrese operacion")

#codigo
if operacion == "suma":
    print("Resultado", suma(valor1, valor2))
elif operacion == "resta":
    print("Resultado", resta(valor1, valor2))

# falta hacer el producto y el cociente
