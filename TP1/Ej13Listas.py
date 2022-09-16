'''
El usuario deberá pensar en uno de los siguientes personajes: Lio Messi, Mauricio
Macri y Mirtha Legrand. El programa mediante algunas preguntas convenientes
(edad, sexo, ocupación, etc.) deberá mostrar de que personaje se trata. Ejemplo: si
es hombre y deportista tendrá que decir Lio Messi
'''

nombres = ["Lio Messi", "Mauricio Macri", "Mirtha Legrand"]
edades = [35, 63, 95]
ocupaciones = ["futbolista", "Político", "Conductor/a de TV"]
personajes = list(zip(nombres, edades, ocupaciones))
# print(datos_objetos)  #para ver lista de tuplas
print("datos para jugar:")
for i in range(0,len(personajes)): print(personajes[i])

print("piense en un personaje...")

edad = int(input("¿Qué edad tiene? (copiar y pegar)\n"))
ocupacion = input("¿Cuál es su ocupación? (copiar y pegar)\n")

i = 0
for personaje in personajes:
	if personajes[i][1] == edad and personajes[i][2] == ocupacion:
		print("¿Ud. está pensando en {}?".format(personajes[i][0]))
		break
	i = i + 1

if i == len(personajes):
	print("No se me ocurre nada")
