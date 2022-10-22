'''
Realizar un programa para jugar al ahorcado.

En el programa hay definido un array, que en cada posición tiene una letra.
Todo el array forma la palabra a adivinar.

El usuario debe ingresar las letras que arriesga. Si acierta se ira completando
otro array de la misma longitud que el primero, inicialmente tiene un guion
en cada posición.

Cuando el usuario adivina una letra se reemplaza el guion por la letra,
y se muestra como quedo el array, si no adivina se le informa que
no acertó y se descuenta un intento.

Se debe finalizar o porque adivino la palabra o porque se le acabaron
los intentos, tiene 10 intentos inicialmente,
en el caso de adivinar una letra no se descuenta el intento.
'''

array_secreto = ['a','j','e','d','r','e','z']

array_adivinado = []
for i in range(0, len(array_secreto)):
    array_adivinado.append('-')
#print(array_adivinado)

intentos = 10
while intentos > 0 and array_adivinado != array_secreto:
    intento = input("Ingrese una letra para adivinar la palabra secreta: ")
    letra_en_array = False
    i = 0
    while i < len(array_secreto):
        if array_secreto[i] == intento:
            array_adivinado[i] = array_secreto[i]
            letra_en_array = True
        i = i + 1
    if letra_en_array == True:
        print("Acertaste!")
        print(array_adivinado)
    if letra_en_array == False:
        print("No acertaste :(")
        intentos = intentos -1

if intentos == 0:
    print("Perdiste :_(")
else:
    print("Ganaste!!! :D")
