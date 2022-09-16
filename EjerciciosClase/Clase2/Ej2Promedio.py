gasto_total = 0
semana = 1
while semana < 5:
    gasto = float(input(""))
    gasto_total = gasto + gasto_total
    semana = semana + 1
promedio = gasto_total/4
