
num1 = int(input("Ingresar primer número: "))
num2 = int(input("Ingresar segundo número: "))

print("Menú principal\n"
      "1. Sumar\n"
      "2. Restar\n"
      "3. Multiplicar\n"
      "4. Dividir\n"
      "5. Salir")
opc = int(input("Seleccione una opción: "))

if opc == 1:
    res = num1 + num2
elif opc == 2:
    res = num1 - num2
elif opc == 3:
    res = num1*num2
elif opc == 4:
    if num2 == 0:
        raise NameError('HiThere')
    else:
        res = num1/num2      
elif opc == 5:
    pass
else:
    pass

print(res)
