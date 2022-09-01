'''
Ingresar un numero de dos cifras, si es mayor que 50 mostrarlo invertido. Sino
mostrar la cifra que corresponde a las unidades.
'''

numero = int(input("Ingrese un número de dos cifras"))
while len(str(numero)) != 2:
	print("Errror")
	numero = int(input("Ingrese un número de dos cifras"))

criterio = 50
if criterio < numero:
	pass
elif numero <= criterio:
	pass
	
