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
ocupaciones ["futbolista", "Político", "Conductor/a de TV"]
# ver como usar zip
print("datos para jugar\n"
	  "nombres: ", nombres,"\n"
	  "edades: ",  edades,"\n"
	  "ocupaciones", ocupaciones,"\n")

# ver como poner esto en un while con nombramiento dinámico, ej "personaje{}".format(i+1) = Personaje(personajes[0]). Hacer antes input edad
personaje1 = Personaje(nombres[0], edades[0], ocupaciones[0])
personaje2 = Personaje(nombres[1], edades[1], ocupaciones[1])
personaje3 = Personaje(nombres[2], edades[2], ocupaciones[2])


print("piense en un personaje...")

edad = int(input("¿Qué edad tiene? (copiar y pegar)\n"))
ocupacion = input("¿Cuál es su ocupación? (copiar y pegar)")
#combinatoria
