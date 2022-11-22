
def promedio(arreglo):
    n = len(arreglo)
    i = 0
    sumatoria = 0
    while i < len(arreglo):
        sumatoria = sumatoria + arreglo[i]
        i = i+1
    if n != 0:
        prom = sumatoria/n
        return prom
    else:
        raise ZeroDivisionError


## test

arr = []
print(arr)
try:
    promedio(arr)
except ZeroDivisionError:
    print('Error en tiempo de ejecución')

arr = [5,4,6,8,7,9,1,9,9,9,8]
prom = promedio(arr)
print(arr)
print(prom)

