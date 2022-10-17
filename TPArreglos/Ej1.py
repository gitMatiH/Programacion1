notas = [7, 5, 9, 6, 2, 9, 10]

print(notas[6])
print(notas[0])
print(notas[2])
print(notas[4])
print(notas[-1])

print(notas)

indice = 0

while indice < 7:
    print(notas[indice])
    indice = indice + 1

posicion = int(input("Ingrese posición: "))
if posicion < 7:
    print(notas[posicion-1])
else:
    print("Error.")

## puedo "medir" el array. Se puede auto-identificar y presentar sus propiedades
# usando:
len(notas)
