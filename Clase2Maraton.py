'''Se quiere validar el registro a una maratón para ello 
se pide como datos nombre, edad y género. 
El cupo máximo es de 30 participantes. 
Si son mayores a 35 la categoría es mayores si no, menores. 
Calcular el promedio de edades para los maratonistas femeninos.
Calcular la edad mínima de los participantes masculinos.
Mostrar la cantidad de anotados de categoría mayor.
Calcular cuántos participantes masculinos tienen la edad mínima.
Obtener los nombres de los participantes 
masculinos que tienen la edad mínima.'''

def promedio_edades_f(edades, genero):
    suma_edades=0
    cantidad=0
    for i in range(0, len(edades)):       
        if genero[i]=="F":
            suma_edades=suma_edades+edades[i]
            cantidad+=1
    if cantidad!=0:        
        promedio=suma_edades/cantidad
    else:
        promedio=0
    return promedio

def edad_minima_m(edades, genero):
    i=0
    minima=0
    while i<len(genero) and genero[i]!="M":
        i=i+1
    if i!=len(genero):    
        minima=edades[i]
        for i in range(0, len(edades)):       
            if edades[i]<minima:
                minima=edades[i]
    else:
        minima=0
    return minima    

def mayores(edades):
    cantidad=0
    for i in range(0, len(edades)):
        if edades[i]>35:
            cantidad =cantidad +1
    return cantidad        
def cuantos_edad_minima(edad_minima, edades, genero):
    cantidad=0
    for i in range(0, len(edades)):
        if edades[i]==edad_minima and genero[i]=="M":
            cantidad=cantidad+1
    return cantidad
def nombres_edad_minima(edad_minima, nombres, edades, genero):
    nombres_minima=[]
    for i in range(0, len(edades)):
        if edades[i]==edad_minima and genero[i]=="M":
            nombres_minima.append(nombres[i])
    return nombres_minima

nombres=[]
edades=[]
genero=[]

for i in range(0,30):
    nombres.append(input("Ingrese nombre del participante"))
    edades.append(int(input("Ingrese edad del participante")))
    genero.append(input("Ingrese genero"))
 
promedio=promedio_edades_f(edades, genero)
if promedio!=0:
    print ("El promedio de edades femeninas es: ",promedio)
else:
    print("No hay participantes femeninas")

edad_minima=edad_minima_m(edades, genero)
if edad_minima!=0:
    print ("La edad minima de los participantes masculinos es: ", edad_minima)
    print ("Hay ", cuantos_edad_minima(edad_minima, edades, genero), " participantes masculinos, con la edad minima" )
    print ("Sus nombres son: ", nombres_edad_minima(edad_minima, edades, nombres, genero))
else:
    print("No participaron varones")
print ("Cantidad de participantes categoria mayores ", mayores(edades))

##credito a las profes
