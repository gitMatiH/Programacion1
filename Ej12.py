'''
Calcular los kilómetros recorridos por un automóvil conociendo el kilometraje inicial
y el actual. Mostrar una leyenda según la distancia recorrida:

Para 100 Km. o menos:			"Paciencia, falta mucho"
Más de 100 Km. y menos de 200:	"Parar para desayunar"
Más de 200 Km.: “Se recomienda:	"Cargar combustible"

'''
import time

km_inicial = int(input("Ingrese el kilometraje inicial que indica el odómetro"))

## simula viaje
i = 0
t_salida = time.time()
while time < 4:
	print("viajando")
	sleep(1)
	i = i + 1
t_llegada = time.time()
t_transcurrido = t_llegada - t_salida
print("Tiempo transcurrido: %s horas" % t_transcurrido )
	
km_actual = int(input("Ingrese el kilometraje inicial que indica el odómetro"))
