

contador = 0
num = int(input("Ingresar número: "))
while num != 0:
    if num > 0:
        contador = contador + 1
    num = int(input("Ingresar número: "))

print("Cantidad de positivos: ", contador)
