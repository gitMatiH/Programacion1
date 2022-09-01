aux = True
while aux == True:
	num1 = int(input('Ingrese numero: '))
	if num1 > 0:
		print("Es positivo!!")
	else:
		if num1 < 0:
			print("Es negativo!!")
		else:
			print("Es cero!!")
	aux1 = str(input("Quiere seguir? y/n\n"))
	#print(aux1)
	if aux1 == "y":
		aux = True
	if aux1 == "n":
		aux = False
	#while not(aux1 == "y" or aux1 == "n"):
	while (aux1 != "y" and aux1 != "n"):# == True: hace esto. si queremos darlo vuelta como override hacemos == False
		print("Comando inválido.")
		aux1 = str(input("Quiere seguir? y/n\n"))
		if aux1 == "y":
			aux = True
			break
		if aux1 == "n":
			aux = False
			break
print("gracias")
