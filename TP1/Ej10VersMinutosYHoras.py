
valorHora = 45
minHora = 1

horas = int(input("Ingrese las horas de estacionamiento acumuladas: "))
minutos = int(input("ingrese los minutos de estacionamiento restantes: "))

if horas < 1:
    print("Se cobra: ", minHora*valorHora)
else:
    if minutos > 15:
        horas = horas + 1
        importe = horas * valorHora
        print("importe:", importe)
    else:
        importe = horas * valorHora
        print("importe:", importe)
