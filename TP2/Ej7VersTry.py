'''
Leer dos números, mostrar el siguiente menú
pudiendo seleccionar alguna opción y
repetir esta operación hasta que seleccione 5.

Menú principal
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Seleccione una opción:
'''

#manejo de errores
def this_fails(num1, num2):
    res = num1/num2
    

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
        try:
            this_fails(num1, num2)
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)        
elif opc == 5:
    pass
else:
    pass

print(res)
