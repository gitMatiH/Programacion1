'''
Ingresar las edades de dos personas. Si una de ellas es mayor de edad y la otra menor
de edad, calcular y mostrar su promedio. En caso contrario mostrar las dos edades.
'''

edad_pers1 = int(input("Ingrese la edad de la primer persona:"))
edad_pers2 = int(input("Ingrese la edad de la segunda persona:"))

def es_mayor_edad(edad):
	edad = int(edad)	#por si viene como string
	if edad >= 18:
		return True
	else:
		return False

if es_mayor_edad(edad_pers1) or es_mayor_edad(edad_pers2):
	promedio_edades = (edad_pers1 + edad_pers2)/2
	print("El promedio de edades es:", promedio_edades)
else:
	print("Edad de la primer persona:", edad_pers1)
	print("Edad de la segunda persona:", edad_pers2)
