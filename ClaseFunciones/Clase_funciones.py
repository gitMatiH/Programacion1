
num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))

###Meto esto en una funcion
##if num1>num2:
##    print("menor ", num1)
##elif num1 == num2:
##    print("Son iguales")
##else:
##    print("menor ", num2)

def menor(num1, num2):
    if num1<num2:
        print("menor ", num1)
    elif num1 == num2:
        print("Son iguales")
    else:
        print("menor ", num2)

menor(num1, num2)

## a partir de ahora acordamos estructurar SIEMPRE
## nuestro código de la manera:
#funciones
#declaracion de variables
#codigo

# o sea:

#funciones
def menor(num1, num2):
    if num1<num2:
        print("menor ", num1)
    elif num1 == num2:
        print("Son iguales")
    else:
        print("menor ", num2)

#declaracion de variables
num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))

#codigo
menor(num1, num2)

## otra forma de usarlo: recibo parámetros y devuelve
## el resultado mediante la sentencia return <>


# ejemplo 2
def suma(num1, num2):
    return(num1 + num2)

##def suma(num1, num2):
##    res = num1 + num2
##    return res

suma_nums = 0
num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))

suma_nums = suma(num1, num2)
print(suma_nums)


# ejemplo 3
def suma(num1, num2):
    res = 0
    res = num1 + num2
    return res

suma_nums = 0
num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))

suma_nums = suma(num1, num2)
print(suma_nums)


### Revisar esto
## una variable si cambia dentro de una funcion,
## no cambia afuera, tengo que trabajar c return
## en cambio, una lista sí. y no necesito return


