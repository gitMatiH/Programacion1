'''
Ingresar dos números, calcular y mostrar el cociente del primero por el segundo,
siempre que el divisor no sea cero. En este último caso mostrar la leyenda “no se
puede realizar el cociente”.
'''

num1 = float(input("Ingrese primer número"))
num2 = float(input("ingrese segundo número"))

print("Calculo cociente de primero por segundo:\n")

if num2 != float(0):
	cociente = num1/num2
	print("El cociente es:", cociente)
else:
	print("no se puede realizar el cociente")
