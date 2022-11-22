
def promedio(arreglo):
    n = len(arreglo)
    i = 0
    sumatoria = 0
    while i < len(arreglo):
        sumatoria = sumatoria + arreglo[i]
        i = i+1
    try:
        prom = sumatoria/n
        return prom
    except ZeroDivisionError:
        print("arreglo vacío")

## test

arr = []
print(arr)
prom1 = promedio(arr)
print(prom1)

arr = [5,4,6,8,7,9,1,9,9,9,8]
print(arr)
prom2 = promedio(arr)
print(prom2)
