'''
10) Leer un número y calcular la suma de los números naturales hasta ese número.
Modificar el algoritmo para que se pueda procesar muchos números. Dar por
terminada la entrada cuando el número sea 0.
'''
num = int(input("ingrese un número: "))
i = 0
sumatoria = 0
while num != 0:
    for i in range(0, num+1):
        print(sumatoria, "+", i)
        sumatoria = sumatoria + i
    print("Resultado de la sumatoria: ", sumatoria)
    num = int(input("ingrese un número: "))
    sumatoria = 0

##vers2
num = int(input("ingrese un número: "))
i=1
sumatoria = 0
while num != 0:
    while i <= num:
        print(sumatoria, "+", i)
        sumatoria = sumatoria + i
        i = i+1
    print("Resultado de la sumatoria: ", sumatoria)
    num = int(input("ingrese un número: "))
    i=1
    sumatoria = 0
