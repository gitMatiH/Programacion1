'''
Se quiere generar una estadística de búsquedas en Internet
y para ello se requiere la siguiente información:
Palabra clave
Cantidad de búsquedas en Argentina
Cantidad de búsquedas en el resto del mundo

La carga de datos finaliza cuando se ingresa la palabra FIN
en la palabra clave

Se pide
-Mostrar la palabra clave que tiene más búsquedas en la Argentina
-Calcular y mostrar el promedio de búsquedas en el resto del Mundo
'''

#Ejercicio 1
acumulador_cant_busquedas_resto = 0
contador = 0

##Bloque de ingreso
palabra_clave = input("Ingrese una palabra clave, 'FIN' para finalizar ingreso: ")
####
    
mas_buscada_arg = palabra_clave
cant_mas_buscada_arg = cant_busquedas_arg
while palabra_clave != 'FIN':
    
    cant_busquedas_arg = int(input("Ingrese la cantidad de búsquedas para la palabra clave en argentina: "))
    cant_busquedas_resto = int(input("Ingrese la cantidad de búsquedas para la palabra clave en el resto del mundo: "))
    acumulador_cant_busquedas_resto = acumulador_cant_busquedas_resto + cant_busquedas_resto
    contador = contador + 1
    
    if cant_busquedas_arg > cant_mas_buscada_arg:
        mas_buscada_arg = palabra_clave
        cant_mas_buscada_arg = cant_busquedas_arg
    
    ##Bloque de ingreso
    palabra_clave = input("Ingrese una palabra clave, 'FIN' para finalizar ingreso: ")
    ####

if contador != 0:
    promedio = acumulador_cant_busquedas_resto/contador

print("La palabra clave que tiene más búsquedas en la argentina es: ", mas_buscada_arg)
print("El promedio de búsquedas por palabra en el resto del mundo es: ", promedio)
