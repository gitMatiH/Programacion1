'''
Generar un arreglo P con los 15 primeros números primos. Mostrarlo.
'''
# sería armar la Criba de Eratóstenes, pero dinámica.
# https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes

#cantidad de primos que queremos buscar:
n = 15

arreglo_primos = []
#definimos número primo por:
#un número primo es el que solamente puede ser dividido por uno y el número mismo
#así que arranca por:
num = 1

while len(arreglo_primos)<n:
    #inicializa
    es_primo = True
    j=1    #asi no da falso positivo por divisible por uno, que lo son todos
    #sale cuando falsea la condición de primo
    while j < len(arreglo_primos) and es_primo == True:
        posible_primo = num
        if (posible_primo % arreglo_primos[j])== 0:
            es_primo = False
        j = j + 1
    #si no falsea la condición de primo lo agrega a la lista
    if es_primo == True:
        arreglo_primos.append(num)
    num = num + 1

print(arreglo_primos)
