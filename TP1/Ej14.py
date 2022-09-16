'''
Ingresar un numero de dos cifras, si es mayor que 50 mostrarlo invertido. Sino
mostrar la cifra que corresponde a las unidades.
'''

def invertir_int(num):
    digitos = len(str(num))
    int(num)
    i = 1
    num_inv = 0
    while num // 10 != 0:
        resto = num % 10
        num_inv = num_inv + resto * (10**(digitos-i))
        num = num // 10
        i = i + 1
    resto = num % 10
    num_inv = num_inv + resto * (10**(digitos-i))
	#ver carpeta intro info
    return int(num_inv)

'''
def invertir_str(num):
	num = str(num)
	while num // 10 != 0:
		num_inv =
	return num_inv
def my_function(x):
	return x[::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)
'''

numero = int(input("Ingrese un número de dos cifras: "))
while len(str(numero)) != 2 and 9 < numero: 
	print("Errror")
	numero = int(input("Ingrese un número de dos cifras: "))

if 50 < numero:
	numero_invertido = invertir_int(numero)
	print("Número invertido: ", numero_invertido)
elif numero <= 50:
	print("Cifra de las unidades: ", numero%10)
