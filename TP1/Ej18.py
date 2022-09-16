'''
Según las notas de los tres trimestres, sacar el promedio.
Si el promedio es mayor o igual a seis y la nota del tercer trimestre
es mayor o igual a seis, está aprobado.
Si no, si el promedio es mayor a cuatro, va a diciembre.
Si es menor a cuatro, va a marzo.
'''

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
