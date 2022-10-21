'''
Revertir un arreglo de 16 componentes sobre él mismo, es decir,
poner el primer elemento en el último lugar y el último en el
primer lugar, el segundo en el penúltimo y este en el segundo, etc.
Decir si el arreglo es capicúa.
'''
## Para probarlo con un arreglo aleatorio:
#import random
#arreglo = []
#n = random.randint(10, 20)
#for i in range(0,n):
#    arreglo.append(random.randint(1, 100))
#print("Arreglo de: ", len(arreglo),"elementos")
#print("El arreglo en cuestión:")
#print(arreglo)

#arreglo = [1, 5, 7, 8, 9, 22, 7, 8, 1, 1, 8, 7, 22, 9, 8, 7, 5, 1]
#arreglo capicua de longitud impar
#arreglo = [1,5,3,5,1]
#arreglo capicua de longitud par
#arreglo = [1,5,3,3,5,1]
#arreglo no capicua de longitud impar
arreglo = [1,2,3,5,1]

mitad = len(arreglo)//2
n = len(arreglo)-1
esCapicua = True
#print(esCapicua)
i = 0

### version que corta cuando descubre que no es capicua
##while i <= mitad and esCapicua==True:
##    #print("paso", i)
##    if arreglo[i] != arreglo[n-i]:
##        esCapicua = False
##        print("la variable esCapicua se falseó. esCapicua ==", esCapicua)
##    aux = arreglo[i]
##    arreglo[i] = arreglo[n-i]
##    arreglo[n-i] = aux
##    i = i+1

# version que sigue invirtiendo aunque no sea capicua
while i <= mitad:
    #print("paso", i)
    if arreglo[i] != arreglo[n-i]:
        esCapicua = False
        print("la variable esCapicua se falseó. esCapicua ==", esCapicua)
    aux = arreglo[i]
    arreglo[i] = arreglo[n-i]
    arreglo[n-i] = aux
    i = i+1

print(arreglo)

if esCapicua==True:
    print("El arreglo es capicúa")
else:
    print("El arreglo no es capicúa")
