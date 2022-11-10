#CODIGO POR JULIO CARDENAS

def intercambiar(indice_a, indice_b, arreglo):
    # intercambia elementos según los índices indicados
    aux=arreglo[indice_a]
    arreglo[indice_a] = arreglo[indice_b]
    arreglo[indice_b] = aux

def ordenar(arreglo):
    for j in range(0, len(arreglo)):
        i = j
        pos_menor = i
        menor = arreglo[i]
        #busca menor del subarreglo
        while i < len(arreglo):
            if arreglo[i] < menor:
                pos_menor = i
                menor = arreglo[i]
            i = i+1
        intercambiar(pos_menor,j,arreglo)

def calcular_maximo(a):
    if len(a) > 0:
        maximo = a[0]
        for i in range(len(a)):
            if maximo < a[i]:
                maximo = a[i]    
        return maximo
    elif len(a) == 0:
        return -1

def calcular_porcentaje(len_suc,total):
    if total != 0:
        return (len_suc/total)*100
    elif total <=0:
        return -1

# Código principal

boedo = []
caballito = []

edad = int(input("Ingrese la edad"))

while edad != 0:
    while edad < 0:
       print("Por favor ingrese edad válida") 
       edad = int(input("Ingrese la edad"))
    suc = input("Ingrese la sucursal").upper()
    while suc != "B" and suc != "C":
        suc = input("Ingrese la sucursal").upper()

    if suc == "B":
        boedo.append(edad)
    else:
        caballito.append(edad)
    
    edad = int(input("Ingrese la edad"))
    

maximo_boedo = calcular_maximo(boedo)
maximo_caballito = calcular_maximo(caballito)

if maximo_boedo != -1:
    
    if maximo_boedo > maximo_caballito:
        print("Cantidad de edad máxima de encuestados en boedo",maximo_boedo)
    elif maximo_boedo < maximo_caballito:
        print("Cantidad máxima de encuestados en caballito",maximo_caballito)
    else:
        print("La cantidad de encuestados es la misma",maximo_boedo)
elif maximo_boedo == -1:
    print("ERROR")
    
# Calcular cantidad de encuestados totales
total = len(boedo) + len(caballito)
print("La cantidad de encuestados totales es:",total)    

# Calcular porcentaje encuestados Boedo
porcentaje = calcular_porcentaje(len(boedo),total)
if porcentaje != -1:
    print("El porcentaje es: ",porcentaje)
elif porcentaje == -1:
    print("ERROR")

# Ordenar
#caballito.sort()
ordenar(caballito)
print(caballito)
