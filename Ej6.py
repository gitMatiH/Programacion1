'''
Ingresar un número. Si es positivo, calcular su raíz cuadrada, si es negativo mostrar
su cuadrado y si es cero mostrar “Error. Ha ingresado un valor nulo”.
'''

numero = int(input("Ingresar un número entero no nulo:"))

if numero > 0:
	raizcuad = numero**(1/2)
	print(f"La raíz cuadrada de {numero} es:", raizcuad)
elif numero < 0:
	cuadrado = numero**2
	rint(f"El cuadrado de {numero} es:", cuadrado)
else:
	print("Error. Ha ingresado un valor nulo")
