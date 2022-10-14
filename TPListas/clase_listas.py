notas = [7, 5, 9, 6, 2, 9, 10]

##print(notas[6])
##print(notas[0])
##print(notas[2])
##print(notas[4])
##print(notas[-1])
##
##print(notas)

##indice = 0
##
##while indice < 7:
##    print(notas[indice])
##    indice = indice + 1

##posicion = int(input("Ingrese posición: "))
##if posicion < 7:
##    print(notas[posicion-1])
##else:
##    print("Error.")
##
#### puedo "medir" el array. Se identifica, presenta sus propiedades
##
##print(notas)

indice = -1 #0
posicion = 0
nota = -1
while indice < len(notas):
    if notas[indice] < 4:
        posicion = indice
        nota = notas[indice]
    indice += 1

if posicion == -1:
    print("No hay desaprobados.")
else:
    print("La posicion en el array es:", posicion)
    print("La nota es:", nota)
