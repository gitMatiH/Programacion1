'''
Calcular  el  importe  que  debe  pagar  un  auto  en  un  estacionamiento  
teniendo  en cuenta como datos las horas y minutos de uso. El valor de la hora 
es de $45 y si los minutos exceden de 15 se incrementa una hora al importe. 
El mínimo a cobrar es de una hora.
'''

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
