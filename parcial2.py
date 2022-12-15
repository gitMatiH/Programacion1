def calcularPromedioPorProducto(vec):
    prom = 0
    for i in range(0, len(vec)):
        prom += vec[i]
    if prom>0:
        prom = prom / len(vec)
    return prom

def calcularMontoGanado(vec, producto, dia):
    if producto=="Net":
        precio=690
    elif producto=="Not":
        precio=985
    elif producto=="Tab":
        precio=525
    monto=(vec[dia]*precio)
    return monto

def calcularMayor(montoA, montoB, montoC):
    mayor=0
    if montoA>montoB and montoA>montoC:
        mayor=montoA
    elif montoB>montoA and montoB>montoC:
        mayor=montoB
    else:
        mayor=montoC
    return mayor

def calcularProdMenosVendido(vec):
    diaMenosVentas = 0
    cantMenos=vec[0]
    for i in range(0, len(vec)):
        if vec[i]<cantMenos:
            cantMenos=vec[i]
            diaMenosVentas=i
    return diaMenosVentas

vecNET = []
vecNOTB = []
vecTAB = []

for j in range(0, 2):
    cantNet = int(input("Ingrese la cantidad de Netbooks vendidas en el dia: "))
    while cantNet<0:
        int(input("Ingrese la cantidad de Netbooks vendidas en el dia: "))
    vecNET.append(cantNet)
    cantNotb = int(input("Ingrese la cantidad de Notebooks vendidas en el dia: "))
    while cantNotb<0:
        int(input("Ingrese la cantidad de Notebooks vendidas en el dia: "))
    vecNOTB.append(cantNotb)
    cantTab = int(input("Ingrese la cantidad de Tablets vendidas en el dia: "))
    while cantTab<0:
        int(input("Ingrese la cantidad de Tablets vendidas en el dia: "))
    vecTAB.append(cantTab)

    montoNet=calcularMontoGanado(vecNET, "Net", j)
    montoNot=calcularMontoGanado(vecNOTB, "Not", j)
    montoTab=calcularMontoGanado(vecTAB, "Tab", j)

    mayorMontoDelDia=calcularMayor(montoNet, montoNot, montoTab)
    if mayorMontoDelDia==montoNet:
        prodMasGanancia = "Netbooks"
    elif mayorMontoDelDia == montoNot:
        prodMasGanancia = "Notebooks"
    else:
        prodMasGanancia = "Tablets"

    print("El mayor monto ganado del dia es del producto ", prodMasGanancia, " con un monto de ", mayorMontoDelDia, " en el dia numero ", j+1)

producto=input("Ingrese el producto para ver el dia menos vendido")
if producto == "Net":
    diaMenosVendido=calcularProdMenosVendido(vecNET)
    montoDiaMenosVendido=calcularMontoGanado(vecNET, "Net", diaMenosVendido)
if producto == "Not":
    diaMenosVendido=calcularProdMenosVendido(vecNOTB)
    montoDiaMenosVendido=calcularMontoGanado(vecNOTB, "Not", diaMenosVendido)
else:
    diaMenosVendido=calcularProdMenosVendido(vecTAB)
    montoDiaMenosVendido=calcularMontoGanado(vecTAB, "Tab", diaMenosVendido)

print("El dia que menos se vendio ", producto, " fue ", diaMenosVendido+1)
print("El monto del dia que menos se vendio fue ", montoDiaMenosVendido)

for i in range(0, len(vecTAB)):
    for x in range(0, len(vecTAB)-1):
        if vecTAB[x]<vecTAB[x+1]:
            aux = vecTAB[x]
            vecTAB[x]=vecTAB[x+1]
            vecTAB[x+1]=aux
print(vecTAB)

promedioNet = calcularPromedioPorProducto(vecNET)
print("El promedio de productos vendidos de Netbooks es: ", promedioNet)
promedioNotb = calcularPromedioPorProducto(vecNOTB)
print("El promedio de productos vendidos de Notebooks es: ", promedioNotb)
promedioTab = calcularPromedioPorProducto(vecTAB)
print("El promedio de productos vendidos de Tablets es: ", promedioTab)
