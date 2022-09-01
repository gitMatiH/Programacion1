# Calcular el sueldo de una persona, conociendo la cantidad de horas que trabaja en
# el mes y el valor de la hora.

horas = int(input("ingrese cantidad de horas trabajadas en el mes:\n"))

valorhora = float(input("ingrese el valor de una hora de trabajo\n"))

sueldo = horas*valorhora    #autocastea a float, hace un uptype del int

print("sueldo:", sueldo)

# Calcular el importe que debe pagar una persona compra una heladera de pesos X y
# por pagar en efectivo le hacen el 10% de descuento ¿Cuánto abona?

precio_heladera = float(input("Ingrese el precio de la heladera:\n"))

efectivo = input("ingrese si pagó en efectivo y/n:\n")
while efectivo != "y" and efectivo != "n":
    print("comando inválido.")
    efectivo = input("ingrese si pagó en efectivo y/n:\n")

if efectivo == "y":
    print("Obtiene 10 por ciento de descuento")
    descuento = 10 * precio_heladera / 100
    abona = precio_heladera - descuento
    print("El cliente abona:", abona)
elif efectivo == "n":
    abona = precio_heladera
    print("El cliente abona:", abona)

# Convertir longitudes de millas a Km. y de pulgadas a cm., si:
# 1 milla = 1.60935 Km.
# 1 pulgada = 2.534 cm.

eleccion = input("ingrese pulgadas (p) o millas (m):\n")
if not(eleccion == "p" or eleccion == "m"): #equiv: eleccion != "p" and eleccion != "m"
    print("comando inválido.")
    eleccion = input("ingrese pulgadas (p) o millas (m):\n")

if eleccion == "p":
    pulgadas = float(input("Ingrese cuántas pulgadas a convertir a centímetros:\n"))
    res = (pulgadas*2.534)/1
    print("son", res, "centímetros")
elif eleccion == "m":
    millas = float(input("Ingrese cuántas millas a convertir a kilómetros:\n"))
    res = (millas*1.60935)/1
    print("son", res, "kilómetros")

# Hallar la longitud de la hipotenusa de un triángulo dada la medida de sus catetos

print("El triángulo debe ser rectángulo")
cateto1 = float(input("ingrese cateto 1"))
cateto2 = float(input("ingrese cateto 2"))

hipotenusa = cateto1^2+cateto2^2
print("la hipotenusa es: ", hipotenusa)

# Calcular  el  importe  que  debe  pagar  un  auto  en  un  estacionamiento  
# teniendo  en cuenta como datos las horas y minutos de uso. El valor de la hora 
# es de $45 y si los minutos exceden de 15 se incrementa una hora al importe. 
# El mínimo a cobrar es de una hora.

valorHora = 45
minHora = 1
minutos = int(input("ingrese cuantas minutos estuvo estacionado"))

horas = 0

if minutos < 60:
    print("Se cobra: ", minHora*valorHora)

while minutos > 60:
    minutos = minutos - 60
    horas = horas + 1

if minutos > 15:
    horas = horas + 1
    importe = horas * valorHora