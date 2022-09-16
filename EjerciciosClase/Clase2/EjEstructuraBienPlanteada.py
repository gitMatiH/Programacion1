###estructura bien planteada:   if para procesar info. Con pregunta estilo seguir? no sería la estructura correcta
##numero = int(input(""))
##while numero != 0:
##
##
##    numero = int(input(""))

cantidad = 0
numero = int(input("Ingrese numero, 0 para terminar: "))
while numero != 0:
    if numero > 0:
        cantidad = cantidad + 1
    numero = int(input("Ingrese numero, 0 para terminar: "))
print("Cantidad de numeros positivos: {}".format(cantidad))
