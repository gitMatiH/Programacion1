##Ver siempre alguna plantilla pythonic para ver la manera pythonic de hacerlo

class Bingo:
    def jugar_de_nuevo(self):
        j = input("¿Quieres volver a jugar? Responde si/no: ")
        while True:
            if (j == "si"):
                return True
            elif (j == "no"):
                return False
            else:
                j = input("Por favor, introduce un valor válido: ")

    def jugar(self):
        while True:
            juego_activo = True
            while juego_activo:
                print("Jugando")
                print("Terminó el juego")
                juego_activo = False

            if self.jugar_de_nuevo():
                print("Volvemos a jugar.")
            else:
                print(f"Adios. ¡¡¡Vuelve pronto!!!")    #podemos preguntar el nombre al ppio y poner adios {nombre}
                break


juego = Bingo()
print(juego.jugar())
