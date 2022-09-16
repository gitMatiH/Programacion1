
print("Calcula la retención en base a ganancias.")

ganancias = int(input ("ingrese sus ganancias anuales:\n"))
if ganancias <= 10000:
    print ("Retencion = cero")
elif 10000 < ganancias and ganancias <= 15000:
    retencion = (ganancias - 10000)*2/100
    print ("Retencion = ", retencion)
else:   #usa la condición que queda por descarte, en este caso ganancias > 150000
    retencion = 300 + (ganancias - 15000)*5/100
    print ("Retencion = ", retencion)
