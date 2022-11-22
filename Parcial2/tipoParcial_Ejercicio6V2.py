'''
Ejercicio 6

Ingresar valores numéricos enteros hasta cargar un arreglo con los 8
primeros números pares múltiplos de 3. Mostrarlo.


a. Mostrar los 2 valores más pequeños múltiplos de 6. Si no los hubiese,
mostrar una leyenda.

b. Eliminar del arreglo aquellos valores menores a su promedio.

c. Insertar en dicho arreglo después de cada numero, su doble.
'''

def ranking_2(array):
    # busca los dos menores en un array
    if len(array)==0:
        sal = "Array vacío"
        return sal
    elif len(array)==1:
        sal = array[0]
        return sal
    else:
        ranking = []
        ## pongo el primero dos veces para inicializar un ranking de dos con
        ## un elemento dentro del conjunto del array
        ranking.append(array[0])
        ranking.append(array[0])
        i = 1
        while i<len(array):
            if array[i]<ranking[len(ranking)-1] or ranking[0]==ranking[1]:
                # si tuviésemos un ranking de tres serían los tres iguales
                # y hay que llenar los dos ultimos con el numero nuevo
                # lo mismo para n
                # hay que llenar los m-1 ultimos con el numero nuevo
                j = len(ranking)-1
                ranking[j] = array[i]
                while ranking[j]<ranking[j-1] and j > 0:
                    intercambiar(j,j-1,ranking)
                    j = j-1
            i = i+1
        return ranking
def intercambiar(i,j,array):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux

'''
### Comentar para test
numeros = []

numero = int(input("Ingrese un número entero: "))

while len(numeros) < 8:

    if numero%2==0 and numero%3==0:
        numeros.append(numero)

    numero = int(input("Ingrese un número entero: "))
### Comentar para test
'''

### descomentar para test
numeros=[60,24,6,48,12,36,72,84]

ranking=ranking_2(numeros)
print("Lista:",numeros)
print("Ranking menores:",ranking)




'''
depurando

Ingrese un número entero: 6
Ingrese un número entero: 12
Ingrese un número entero: 48
Ingrese un número entero: 24
Ingrese un número entero: 3
Ingrese un número entero: 24
Ingrese un número entero: 60
Ingrese un número entero: 72
Ingrese un número entero: 84
Ingrese un número entero: 84
Lista: [6, 12, 48, 24, 24, 60, 72, 84]
Ranking menores: [6, 6]
>>>

'''
