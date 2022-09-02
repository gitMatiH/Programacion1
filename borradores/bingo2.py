##Ver siempre alguna plantilla pythonic para ver la manera pythonic de hacerlo
## ver algun video de __main__ y los dobles __ en alguna lista o video que me haya guardado

class Bingo:
    def jugar(self):
        # ....

        self.iniciar_juego()
        while True:
            j = input("¿Quieres volver a jugar? Responde si/no: ")
            while True:
                if (j == "si"):
                    print("Volvemos a jugar.")
                    self.iniciar_juego()
                    break   #el break se refiere a qué? al if, al while en el que esta anidado??
                elif (j == "no"):
                    print(f"Adios {nombre}. ¡¡¡Vuelve pronto!!!")
                    break
                else:
                    j = input("Por favor, introduce un valor válido: ")

    def iniciar_juego(self):
        juego_activo = True
        while juego_activo:
            print("Jugando")
            print("Terminó el juego")
            juego_activo = False


juego = Bingo()
print(juego.jugar())
