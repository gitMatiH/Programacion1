#Implementación Quicksort

##def quicksort(l):
def quicksortRec(l, i, j):
    if i < j:
        k = particion(l, i, j)
        quicksortRec(l, i, k-1)
        quicksortRec(l, k+1, j)
    quicksortRec(l, 0, len(l)-1)

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

##l = list(input("ingrese una lista de enteros"))
##print(l)
##print(type(l))
##while type(l)!= list():
##    print("ingreso erróneo")
##    l = input("ingrese una lista de enteros")

l=[8,5,4,10,-1]
print(l)
i=0
j=len(l)
quicksortRec(l,i,j)
print(l)
