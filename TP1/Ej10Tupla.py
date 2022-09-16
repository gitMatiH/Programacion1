# Version con tupla

# Toma valores por tuplas
valores = input('Ingresar tupla de valores (horas, minutos), separado por espacio: ')
cronometro = tuple(valores.split())     # Separa los valores del input por el caracter 'espacio' y forma una lista,
                                        # luego pasa la información a tipo 'tupla'

print('Tupla de entrada: ', cronometro)  # cronometro es una tupla de cadena de caracteres

valorHora = 45
minHora = 1

if int(cronometro[0]) < 1:
    print("Se cobra: ", minHora*valorHora)
else:
    if int(cronometro[1]) > 15:
        horas = int(cronometro[0]) + 1
        importe = horas * valorHora
        print("importe:", importe)
    else:
        importe = int(cronometro[0]) * valorHora
        print("importe:", importe)
