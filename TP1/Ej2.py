'''
Calcular el importe que debe pagar una persona compra una heladera de pesos X y
por pagar en efectivo le hacen el 10% de descuento ¿Cuánto abona?
'''

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
