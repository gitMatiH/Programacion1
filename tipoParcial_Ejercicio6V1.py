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
        menor = array[0]
        menor2 = array[0]
        i = 1
        while i<len(array):
            if array[i]<menor and array[i]<menor2:
                menor=array[i]
            elif array[i]<menor2:
                menor2=array[i]
            i = i+1
        return menor, menor2


### Comentar para test
numeros = []

while len(numeros) < 8:

    numero = int(input("Ingrese un número entero: "))
    
    if numero%2==0 and numero%3==0:
        numeros.append(numero)

### Comentar para test


### descomentar para test
#numeros=[60,24,6,48,12,36,72,84]

ranking=ranking_2(numeros)
print("Lista:",numeros)
print("Ranking menores:",ranking)


