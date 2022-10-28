from lib2to3.refactor import MultiprocessRefactoringTool


def promedio(ventas):
    suma=0
    for i in range(0, len(ventas)):
        suma+=ventas[i]
    return suma/len(ventas)
def menor(num1, num2,num3):
    if num1<num2 and num1<num3:
        return "Enero"
    elif num2<num1 and num2<num3:
        return "Febrero"
    return "Marzo"        
def menor1(valores, meses):
    minimo=valores[0]
    posicion=0
    for i in range(1, len(valores)):
        if minimo>valores[i]:
            minimo=valores[i]
            posicion=i
    return meses[posicion]        
    '''if i==0:
        return "Enero"
    elif i==1:
        return "Febrero"
    return "Marzo"           '''

# Encontrar el mes con menor promedio de ventas
promedios=[]
meses=[]
ventas_enero=[1000,1300.50,2500,1350.80]
ventas_febrero=[580.30,980,2560.50,1500]
ventas_marzo=[1290.60,2570,3500.50,1670]
'''promedio_enero=promedio(ventas_enero)
promedio_febrero=promedio(ventas_febrero)
promedio_marzo=promedio(ventas_marzo)
mes_menor=menor(promedio_enero, promedio_febrero, promedio_marzo)'''
promedios.append(promedio(ventas_enero))
meses.append("Enero")
promedios.append(promedio(ventas_febrero))
meses.append("Febrero")
promedios.append(promedio(ventas_marzo))
meses.append("Marzo")
mes_menor=menor1(promedios,meses)