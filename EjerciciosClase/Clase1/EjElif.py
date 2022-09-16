edad = int(input("ingresa tu edad:\n"))


if edad >= 18:
	print("Es mayor de edad")
else:
	print("No es mayor de edad")



if edad < 8:
	print("No paga")
else:   #solo se que es menor a 8
    if edad < 12:
        print("paga 50%")
    else:
        if edad < 18:
            print("paga 70%")
        else:
            print("paga total")

if edad < 8:
    print("No paga")
elif edad < 12: #solo se que es menor a 8
    print("paga 50%")
elif edad < 18:
    print("paga 70%")
else:   #el else siempre va sin condicion
    print("paga total")
