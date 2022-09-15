'''
5) Leer el número de mes y mostrar cuantos
días tiene ese mes (año actual).
'''
## Ver carpeta

diasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

'''
Un año es bisiesto si es:

Divisible entre 4.
Y
(No divisible entre 100.
O
Divisible entre 400.)
'''
# input(mes, anio) (ver tupla)

def EsBisiesto(anio):
    if anio % 4 == 0 and (anio%100 != 0 or anio%400==0):
        return True
    else:
        return False

mes = int(input("ingrese mes: "))
anio = int(input("ingrese año: "))

if EsBisiesto(anio)==True:
    if mes == 2:
        print("el mes tiene ", diasMes[mes-1]+1,"días")
else:
    print("el mes tiene", diasMes[mes-1],"días")
