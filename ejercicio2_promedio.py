def inicializar_matriz(filas, columnas):
	matriz = []
	for i in range(0, filas):
		matriz.append([0 for j in range(0, columnas)])
	print("matriz", matriz)
	return matriz

num = int(input("Indique cuántas personas va a ingresar:\n"))	#porque por defecto lee un string
if num >= 1:
	#inicializar_matriz(num, salida matriz)
	filas, columnas = (num,2)
	datos = inicializar_matriz(filas, columnas)
	print("datos", datos)
	for i in range(0, num):
		print("vamos por la persona numero:",i+1)
		print("Ingrese nombre de la persona",i+1,":")
		nombre = str(input())
		datos[i][0] = nombre
		print(datos)
		print("Ingrese edad de",nombre,":")
		edad = input()
		datos[i][1] = int(edad)
		print(datos)

	print("base de datos",datos)

	#Busca Mayor
	mayor = 0
	for i in range(num):
		if int(datos[i][1]) > int(datos[mayor][1]):
			mayor = i
	
	pers = datos[mayor][0]
	print("la persona mayor es", pers)

	#Hace promedio
	acum = 0
	for i in range(num):
		dato = datos[i][1]
		acum =  acum + dato

	prom = acum/num

	print("El promedio de edades es", prom)
else:
	pass
