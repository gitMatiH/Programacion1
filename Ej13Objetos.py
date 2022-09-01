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
print("\nDatos para jugar:")
for i in range(0,len(datos_objetos)): print(datos_objetos[i])

personajes = []
for i in range(0, len(datos_objetos)):
    datos_personaje = datos_objetos[i]
    nombre, edad, ocupacion = datos_personaje
    print("\nPersonaje procesado: ", nombre)
    personaje = Personaje(nombre, edad, ocupacion)
    personajes.append(personaje)
    ##tambien vale insert en vez de append:
    #personajes.insert(-1, personaje)
    print("Lista actual de personajes: ")
    for j in range(0, i+1): print(personajes[j].nombre)
print("\nLista total de personajes: ")
for i in range(0, len(personajes)): print(personajes[i].nombre)
print()

print("Piense en un personaje...")

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
