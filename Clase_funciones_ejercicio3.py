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

promedios = []
promedios.append(promedio_enero)
promedios.append(promedio_febrero)
promedios.append(promedio_marzo)

print(promedios)

print()
menor = promedios[0]
indice_menor = 0
print("Recorro lista 'promedios'")
for i in range(0, len(promedios)):
    print(promedios[i])
    if promedios[i]<menor:
       menor = promedios[i]
       indice_menor = i
mes_menor = indice_menor
print()
    
print("El mes de menor promedio está en el índice",
      mes_menor)
print("El mes de menor promedio está en la posición",
      mes_menor+1)
print("El mes del calendario de menor promedio es el mes:",
      mes_menor+1)
