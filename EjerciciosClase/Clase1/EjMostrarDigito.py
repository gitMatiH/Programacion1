numero = int(input("ingrese numero\n"))
i = 1

###version hardcoded
##numero = numero // 10
##numero = numero % 10
##print(numero)

while i!=3:
    resto = numero % 10
    if i == 2:
        print(resto)
    numero = numero // 10
    i = i+1

#otras formas con multiplicacion y restas
