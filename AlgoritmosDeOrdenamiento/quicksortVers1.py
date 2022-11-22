#Implementación Quicksort Vers.1

def quicksort(l, i, j):
    if len(l) == 1:
        return l
    if i < j:
        k = particion(l, i, j)
        quicksort(l, i, k-1)
        quicksort(l, k+1, j)
    return l

def particion(l, i, j):
    x = l[j]
    k = i-1
    for h in range(i,j):
        if l[h] <= x:
            k += 1
            aux  = l[h]
            l[h] = l[k]
            l[k] = aux
    aux = l[k+1]
    l[k+1] = l[j]
    l[j] = aux
    return k+1

l = [int(item) for item in input("ingrese una lista de enteros separados por comas: ").split(",")]
print("lista a ordenar: ", l)
i=0
j=len(l)-1
quicksort(l, i, j)
print("lista ordenada: ", l)
