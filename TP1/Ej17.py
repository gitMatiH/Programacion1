'''
17. Ingresar las medidas de dos ángulos expresados en
grados minutos y segundos y hallar la suma. (recordar
que los minutos y los segundos no deben excederse de 60)
'''

##y version ingreso tuplas??

####version objetos
##poner un objeto con constructor con esto:
##grados = int(input("ingrese los grados del ángulo: "))
##minutos = int(input("ingrese los minutos del ángulo: "))
##while minutos > 60:
##    print("Error: los minutos no pueden ser mayores a 60")
##    minutos = int(input("ingrese los minutos del ángulo: "))
##segundos = int(input("ingrese los segundos del ángulo: "))
##while segundos > 60:
##    print("Error: los segundos no pueden ser mayores a 60")
##    minutos = int(input("ingrese los segundos del ángulo: "))


grados1 = int(input("ingrese los grados del ángulo 1: "))
minutos1 = int(input("ingrese los minutos del ángulo 1: "))
while minutos1 > 60:
    print("Error: los minutos no pueden ser mayores a 60")
    minutos1 = int(input("ingrese los minutos del ángulo 1: "))
segundos1 = int(input("ingrese los segundos del ángulo 1: "))
while segundos1 > 60:
    print("Error: los segundos no pueden ser mayores a 60")
    minutos1 = int(input("ingrese los segundos del ángulo 1: "))

grados2 = int(input("ingrese los grados del ángulo 2: "))
minutos2 = int(input("ingrese los minutos del ángulo 2: "))
while minutos2 > 60:
    print("Error: los minutos no pueden ser mayores a 60")
    minutos2 = int(input("ingrese los minutos del ángulo 2: "))
segundos2 = int(input("ingrese los segundos del ángulo 2: "))
while segundos2 > 60:
    print("Error: los segundos no pueden ser mayores a 60")
    minutos2 = int(input("ingrese los segundos del ángulo 2: "))

print("ángulo 1: {}°, {}\', {}\'\'".format(grados1, minutos1, segundos1))
print("ángulo 2: {}°, {}\', {}\'\'".format(grados2, minutos2, segundos2))

suma_grados = 0
suma_minutos = 0
suma_segundos = 0
## Revisar si la cuenta y lógica están bien
suma_segundos = segundos1+segundos2
if suma_segundos//60 >= 0:
    suma_minutos = suma_minutos + 1
    suma_segundos = suma_segundos%60

suma_minutos = minutos1+minutos2
if suma_minutos//60 >= 0:
    suma_grados = suma_grados + suma_grados//60
    suma_minutos = suma_minutos%60

suma_grados = grados1+grados2

print("El resultado de la suma de ángulos es: {}°, {}\', {}\'\'".format(suma_grados, suma_minutos, suma_segundos))
