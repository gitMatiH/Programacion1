'''
Ingresar la medida de un ángulo y determinar si es agudo, obtuso, recto, nulo o llano.
Si el valor ingresado es mayor a 180º mostrar la leyenda "ángulo no válido" e
ingresar un nuevo valor.
'''

from decimal import Decimal

def anguloInvalido(angulo):
    angulo = Decimal(angulo)    #no interfiere porque pertenece a otro scope
    if abs(angulo) > 180:
        return True
    else:
        return False

def ingresarAngulo():
    angulo = input("Ingrese un ángulo en grados en formato entero o xxx.xxx. Puede ser negativo o nulo.\n")
    while anguloInvalido(str(angulo)):
        print("ángulo no válido")
        angulo = input("Ingrese un ángulo en grados en formato entero o xxx.xxx. Puede ser negativo o nulo.\n")
    return angulo

def analizarAngulo(angulo):
    angulo = Decimal(angulo)
    if angulo == 0:
        return("Ángulo nulo")
    elif abs(angulo) == 180:
        return("Ángulo llano")
    elif abs(angulo) == 90:
        return("Ángulo recto")
    elif abs(angulo) < 90:
        return("Ángulo agudo")
    elif abs(angulo) > 90:
        return("Ángulo obtuso")
    else:
        return("Error")
        #return Exception    #ver excepciones en python


angulo  = ingresarAngulo()
resultado = analizarAngulo(angulo)
print(resultado)




