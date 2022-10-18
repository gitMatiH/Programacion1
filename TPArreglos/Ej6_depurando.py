'''
Se pide cargar en memoria un arreglo de N posiciones.
Se pide generar un programa que emita un ranking con
los 10 números más grandes.
'''

lista = [38, 32, 4, 46, 39, 10, 72, 71, 33, 86, 76, 21, 94, 62, 90, 47, 93, 45, 90, 52, 46, 33, 5, 2, 24, 77]

ranking = []
longitud = 10   # queremos un ranking de diez elem
for i in range(0,longitud):
    ranking.append(lista[i])
print(ranking)
### me faltó ordenar el ranking!!!!!
ranking.sort(reverse=True)
print(ranking)


i = 0
while i < len(lista):
    pos = len(ranking)-1
    elem = lista[i]
    if ranking[pos] < elem:
        ranking[pos] = elem
        while pos > 0 and ranking[pos-1] < ranking[pos]:
            #lista = intercambiar(j-1,j,lista) ¿por que esto no anda?
            aux = ranking[pos-1]
            ranking[pos-1] = ranking[pos]   #promociona
            ranking[pos] = aux
            pos = pos - 1
    i = i + 1
print(ranking)

## Errores
# con un test me dio:
# [94, 93, 90, 90, 77, 52, 38, 32, 4, 46]
# lista de entrada fue:
# [38, 32, 4, 46, 39, 10, 72, 71, 33, 86, 76, 21, 94, 62, 90, 47, 93, 45, 90, 52, 46, 33, 5, 2, 24, 77]
#
# el error se replica, usar debugger
'''
[38, 32, 4, 46, 39, 10, 72, 71, 33, 86]
[4, 10, 32, 33, 38, 39, 46, 71, 72, 86]
[94, 93, 90, 90, 77, 52, 46, 4, 10, 32]

el 4, sigue dando mal
'''

"""

[38, 32, 4, 46, 39, 10, 72, 71, 33, 86]
[86, 72, 71, 46, 39, 38, 33, 32, 10, 4]
[94, 93, 90, 90, 86, 86, 77, 76, 72, 72]

con  el agregado de reverse=True
al ranking.sort()
se solucionó. Descubrí el bug pero no me lo puedo explicar.

"""
