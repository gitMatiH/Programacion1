# encontrar el mes con menor promedio de ventas

ventas_enero    = [1000, 1300, 50, 2500, 1350.80]
ventas_febrero  = [580.30, 980, 2560.50, 1500]
ventas_marzo    = [1290.60, 2570, 3500.50, 1670]

print(ventas_enero)
print(ventas_febrero)
print(ventas_marzo)

#acá sólo la definimos
def promedio_mes(ventas):
    #variables
    acumulador = 0
    contador = 0
    n = len(ventas)
    
    ##procesa
    # adentro del while se van a actualizar las variable
    while contador < n:
        #hace lo que tiene que hacer
        acumulador = acumulador + ventas[contador]
               
        # se actualiza al final
        contador = contador + 1
        # es lo mismo que: contador += 1

    promedio = acumulador/contador
    print(promedio)
    
    ##devuelve cosas
    return (promedio)

def menor(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return "Enero"
    elif num2 < num1 and num2 < num3:
        return "Febrero"
    # else:
    #   return "Marzo"
    # es lo mismo q 
    return "Marzo"


#acá la usamos
promedio_enero = promedio_mes(ventas_enero)
promedio_febrero = promedio_mes(ventas_febrero)
promedio_marzo = promedio_mes(ventas_marzo)

mes_menor = menor(promedio_enero, promedio_febrero,
                  promedio_marzo)

print("El mes de menor promedio de ventas fue: ", promedio)
