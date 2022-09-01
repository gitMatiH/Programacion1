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

'''
## también funciona, más simple:
personaje1 = Personaje(nombres[0], edades[0], ocupaciones[0])
personaje2 = Personaje(nombres[1], edades[1], ocupaciones[1])
personaje3 = Personaje(nombres[2], edades[2], ocupaciones[2])
personajes = [personaje1, personaje2, personaje3]	# lista de objetos personaje
'''

print("piense en un personaje...")

edad = int(input("¿Qué edad tiene? (copiar y pegar)\n"))
ocupacion = input("¿Cuál es su ocupación? (copiar y pegar)\n")


if personaje1.edad == edad and personaje1.ocupacion == ocupacion:
	print("¿Ud. está pensando en {}?".format(personaje1.nombre))
elif personaje2.edad == edad and personaje2.ocupacion == ocupacion:
	print("¿Ud. está pensando en {}?".format(personaje2.nombre))
elif personaje3.edad == edad and personaje3.ocupacion == ocupacion:
	print("¿Ud. está pensando en {}?".format(personaje3.nombre))
else:
	print("No se me ocurre nada")
