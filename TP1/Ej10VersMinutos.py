'''
Calcular  el  importe  que  debe  pagar  un  auto  en  un  estacionamiento  
teniendo  en cuenta como datos las horas y minutos de uso. El valor de la hora 
es de $45 y si los minutos exceden de 15 se incrementa una hora al importe. 
El mínimo a cobrar es de una hora.
'''

valorHora = 45
minHora = 1

minutos = int(input("ingrese cuántos minutos estuvo estacionado: "))

horas = 0

if minutos < 60:
    print("Se cobra: ", minHora*valorHora)
else:
    
    horas = minutos // 60       # total de horas
    minutos = minutos % 60      # minutos restantes, actualiza la variable minutos
    
    '''
    # cálculo alternativo con estructura while
    while minutos >= 60:        # contamos las horas
        minutos = minutos - 60
        horas = horas + 1
    '''

    if minutos > 15:
        horas = horas + 1
        importe = horas * valorHora
        print("importe:", importe)
    else:
        importe = horas * valorHora
        print("importe:", importe)
