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
