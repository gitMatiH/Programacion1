
Print("Ingresar las notas de cada trimestre")
n1 = input("primer trimestre")
n2 = input("segundo trimestre")
n3 = input("tercer trimestre")

promedio = (n1+n2+n3)/3

if p >= 6 and n3 >= 6:
    print("Aprobado")
elif p >= 4:
    print("Diciembre")
else:
    print("Marzo")
