'''
Se han analizado N < 12 temperaturas correspondientes a N variaciones
de volumen cuando la presión es constante.
Datos:
N: cantidad total de temperaturas y volúmenes
T: temperatura
V: volumen
Hallar y mostrar:
    a. Temperatura máxima y mínima registrada.
    b. Volúmenes correspondientes a cada una de ellas.
    c. Ordenar el arreglo de las temperaturas de mayor a menor e imprimirlas.
'''
import random

#n = random.randint(1,11)
n = 8
temperaturas = [24, 31, 22, 54, 12, 5, 6, 16]
volumenes = [12, 56, 34, 16, 34, 58, 1, 45]

t_max = temperaturas[0]
pos_t_max = 1
t_min = temperaturas[0]
pos_t_min = 1
i = 0
while i < len(temperaturas):
    if temperaturas[i] > t_max:
        t_max = temperaturas[i]
        pos_t_max = i+1
    if temperaturas[i] < t_min:
        t_min = temperaturas[i]
        pos_t_min = i+1
    i = i + 1
    
print("Temperaturas:", temperaturas)
print("Volumenes:" , volumenes)
print("La temperatura maxima fue:" , t_max)
print("Y se dio en la posicion:" , pos_t_max)
print("y su volumen correspondiente fue:" , volumenes[pos_t_max-1])

print("La temperatura minima fue:" , t_min)
print("Y se dio en la posicion:" , pos_t_min)
print("y su volumen correspondiente fue:" , volumenes[pos_t_min-1])

print("El arreglo de temperaturas ordenado:")
temperaturas.sort(reverse=True)
print (temperaturas)

