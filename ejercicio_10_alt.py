valorHora = 45
minHora = 1

minutos = int(input("ingrese cuantas minutos estuvo estacionado: "))

horas = 0

if minutos < 60:
    print("Se cobra: ", minHora*valorHora)
else:
    while minutos >= 60: # contamos las horas con el while
        minutos = minutos - 60
        horas = horas + 1

    # hacer con resto

    if minutos > 15:
        horas = horas + 1
        importe = horas * valorHora
        print("importe:", importe)
    else:
        importe = horas * valorHora
        print("importe:", importe)