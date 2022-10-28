''' Ingresar en un array 10 valores, encontrar el mayor
y obtener las posiciones en las que aparece. El mayor se
puede repetir'''
def mayor(datos):
    max=datos[0]
    for i in range(1,len(datos)):
        if max<datos[i]:
            max=datos[i]
    return max        
def pos_mayores(datos, mayor_valor):
    pos=[]
    for i in range(0,len(datos)):
        if datos [i]==mayor_valor:
            pos.append(i)
    return  pos       

valores=[]
for i in range (0,10):
    valores.append(int(input("Ingrese un valor")))
mayor_valor=mayor(valores)    
pos_mayor=pos_mayores(valores, mayor_valor)