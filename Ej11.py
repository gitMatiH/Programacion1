'''
Se ingresa el código de tipo de llamada: 
1. Local 
2. Interurbana 
3. Internacional 
y la duración en minutos de la misma. Si el minuto cuesta $0.25 para la llamada local,
$0.40 para la llamada interurbana y $1.05 para la llamada internacional, diseñar un
algoritmo que permita calcular el monto a pagar por dicha llamada.
'''

precio_minuto_local			= float(0.25)
precio_minuto_interurbano	= float(0.40)
precio_minuto_internacional	= float(1.05)

codigo = input("1: Local\n"
			   "2: Interurbana\n"
			   "3: Internacional\n"
			   "Ingrese código: ")

duracion = input("Ingrese duración de la llamada en minutos: ")

if codigo == "1":
	monto = precio_minuto_local * int(duracion)
elif codigo == "2":
	monto = precio_minuto_interurbano * int(duracion)
elif codigo == "3":
	monto = precio_minuto_internacional * int(duracion)

print("El costo de la llamada es: {} $".format(monto))
