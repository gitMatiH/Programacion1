temperaturas=[]
presiones=[]
max_temp=0
min_temp=0
presion_tmax=0
presion_tmin=0
n=int(input("Ingrese cuantas temperaturas"))
while n>12:
    n=int(input("Ingrese cuantas temperaturas"))
for i in range(0,n):
    temp=int(input("Ingrese temperatura", i+1))
    temperaturas.append(temp)    
    presiones.append(int(input("Ingree la presion", i+1)))
max_temp=temperaturas[0]
min_temp=temperaturas[0]
for i in range(0,len(temperaturas)):
    if max_temp<temperaturas[i]:
        max_temp=temperaturas[i]
        presion_tmax=presiones[i]
    if min_temp>temperaturas[i]:
        min_temp=temperaturas[i]
        presion_tmin=presiones[i]

print("Temperatura minima ", min_temp, " presion ", presion_tmin)
print("Temperatura maxima ", max_temp, " presion ", presion_tmax)

if 10<len(temperaturas):
    temperaturas.pop(10)

    temperaturas.remove(35)
    temperaturas.reverse()
    temperaturas.sort()