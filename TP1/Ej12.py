

import time

km_inicial = int(input("Ingrese el kilometraje inicial que indica el odómetro: "))

## simula viaje
i = 0
t_salida = time.time()
while i < 4:
	print("viajando")
	time.sleep(1)
	i = i + 1
t_llegada = time.time()
t_transcurrido = t_llegada - t_salida
print("Tiempo transcurrido: %s horas" % t_transcurrido )
	
km_actual = int(input("Ingrese el kilometraje que indica el odómetro: "))

km_recorridos = km_actual - km_inicial

print("Ud. recorrió {} kilómetros.".format(km_recorridos))

if km_recorridos <= 100:
	print("Paciencia, falta mucho")
elif 100 < km_recorridos and km_recorridos <= 200:
	print("Parar para desayunar")
elif 200 < km_recorridos:
	print("Cargar combustible")
