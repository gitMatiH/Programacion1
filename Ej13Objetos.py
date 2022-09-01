'''
El usuario deberá pensar en uno de los siguientes personajes: Lio Messi, Mauricio
Macri y Mirtha Legrand. El programa mediante algunas preguntas convenientes
(edad, sexo, ocupación, etc.) deberá mostrar de que personaje se trata. Ejemplo: si
es hombre y deportista tendrá que decir Lio Messi
'''

class Personaje:
	def __init__(self, nombre, edad, ocupacion):
		self.nombre = nombre
		self.edad = edad
		self.ocupacion = ocupacion

nombres = ["Lio Messi", "Mauricio Macri", "Mirtha Legrand"]
edades = [35, 63, 95]
ocupaciones = ["futbolista", "Político", "Conductor/a de TV"]
datos_objetos = list(zip(nombres, edades, ocupaciones))
# print(datos_objetos)  #para ver lista de tuplas
print("datos para jugar:")
for i in range(0,len(datos_objetos)): print(datos_objetos[i])

personajes = []
for i in range(0, len(datos_objetos)):
    datos_personaje = datos_objetos[i]
    nombre, edad, ocupacion = datos_personaje
    print("personaje procesado: ", nombre)
    personaje = Personaje(nombre, edad, ocupacion)
    personajes.append(personaje)
    ##tambien vale insert en vez de append:
    #personajes.insert(-1, personaje)
    print("lista actual de personajes: ", personajes)
print("lista total de personajes: ", personajes)

print("piense en un personaje...")

edad = int(input("¿Qué edad tiene? (copiar y pegar)\n"))
ocupacion = input("¿Cuál es su ocupación? (copiar y pegar)\n")

presencia = False
for personaje in personajes:
    if personaje.edad == edad and personaje.ocupacion == ocupacion:
        print("¿Ud. está pensando en {}?".format(personaje.nombre))
        presencia = True
        break
if presencia == False:
    print("No se me ocurre nada")
