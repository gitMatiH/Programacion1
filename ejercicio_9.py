# edad = int(input("Ingrese edad"))

# if edad >= 8 and edad <= 12:
#     pass
# else:   #tiene menos de ocho o más de doce
#     pass


print("Calcula la retención en base a ganancias.")

ganancias = int(input ("ingrese sus ganancias anuales:\n"))
if ganancias <= 10000:
    print ("retencion = cero")
elif ganancias >10000 and ganancias <= 15000:   # con or estaría mal, podría pasar algo fuera de rango. Aunque el primero lo filtra (creo)
    retencion = 2 * ganancias / 100 #retencion = (ganancia-15000)*0.02
    print ("retencion total = ", retencion)
else:   #usa la condición que queda por descarte, en este caso ganancias > 150000
    retencion = 300 + 5 * ganancias / 100       # retencion = 300 + (ganancia -15000)*0.05
    print ("retencion total = ", retencion)
