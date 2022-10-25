'''
Ejercicio 1:
Se quiere generar un ranking de jugadores de ajedrez
en línea y para ello se requiere la siguiente
información:
usuario del participante
puntaje obtenido
cantidad de partidos jugados

La carga de datos finaliza cuando se ingresa
la palabra en FIN en el usuario.

Se pide:
Mostrar el nombre del participante que jugó
menos partidos.
Calcular y mostrar el puntaje promedio.
'''

usuario = ""
puntaje = 0
partidos = 0
# acumulador
sumatoria_puntajes = 0
# contador
n = 0




'''
asignación: '='
comparación: '==' o '!=' o '<' o '<=' o '>='
'''
##input
usuario = input('ingrese el usuario del participante: ')
'''
if usuario != "FIN":
    partidos = int(input('ingrese numero de partidos jugados'))
    puntaje = int(input('ingrese el puntaje obtenido'))
'''
##
esPrimero = True    #condición de ser el primer usuario ingresado
#print("valor de esPrimero: ", esPrimero)

while usuario != "FIN":
    
    partidos = int(input('ingrese numero de partidos jugados: '))
    puntaje = int(input('ingrese el puntaje obtenido: '))
    if esPrimero == True:
        #print("valor de esPrimero, después de comparar con True: ", esPrimero)
        usuario_menos_partidos = usuario
        cantidad_menos_partidos = partidos
        esPrimero = False
        #print("valor de esPrimero, después de asignar: ", esPrimero)

    ## procesa
    sumatoria_puntajes = sumatoria_puntajes + puntaje
    n = n+1

    
    ## acá comparamos
    if cantidad_menos_partidos > partidos:
        usuario_menos_partidos = usuario
        cantidad_menos_partidos = partidos
        

    ## termino de procesar
    
    ##input
    usuario = input('ingrese el usuario del participante: ')
    '''
    if usuario != "FIN":
        partidos = int(input('ingrese numero de partidos jugados'))
        puntaje = int(input('ingrese el puntaje obtenido'))
    '''
    ##


print("el usuario con menos partidos es: " , usuario_menos_partidos)
print("Y su cantidad de partidos fue: " , cantidad_menos_partidos)

promedio = sumatoria_puntajes/n
print("El promedio de los puntajes es: " , promedio)
