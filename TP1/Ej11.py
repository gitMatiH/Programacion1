
precio_minuto_local			= float(0.25)
precio_minuto_interurbano	= float(0.40)
precio_minuto_internacional	= float(1.05)

codigo = input("Códigos de tipo de llamada:\n"
			   "1: Local\n"
			   "2: Interurbana\n"
			   "3: Internacional\n\n"
			   "Ingrese código: ")

duracion = input("Ingrese duración de la llamada en minutos: ")

if codigo == "1":
	monto = precio_minuto_local * int(duracion)
elif codigo == "2":
	monto = precio_minuto_interurbano * int(duracion)
elif codigo == "3":
	monto = precio_minuto_internacional * int(duracion)

print("El costo de la llamada es de: {} $".format(monto))
