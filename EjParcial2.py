'''
Ejercicio 2) 
Desarrollar un algoritmo que permita ingresar números enteros hasta que
dicho número sea cero o un número negativo y mostrar:
a) El valor mínimo impar.
b) El promedio de números pares múltiplos de 5.
c) El valor máximo par.
'''

num = int(input("Ingrese un número entero: "))

sumatoria_par_multiplo_cinco = 0
cant_par_multiplo_cinco = 0

max_par = num
min_impar = num

while num > 0:

    if num % 2 == 0:
        if num >= max_par:
            max_par = num
        if num % 5 == 0:
            sumatoria_par_multiplo_cinco = sumatoria_par_multiplo_cinco + num
            cant_par_multiplo_cinco = cant_par_multiplo_cinco + 1
    else:
        if num <= min_impar:
            min_impar = num
    
    num = int(input("Ingrese un número entero: "))

print("Mínimo impar: ", min_impar)
print("Máximo par: ", max_par)

if cant_par_multiplo_cinco > 0:
    promedio_par_multiplo_cinco = sumatoria_par_multiplo_cinco / cant_par_multiplo_cinco
    print("Promedio de números pares múltiplos de 5: ", promedio_par_multiplo_cinco)
