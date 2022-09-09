###Ej1
##nroAlumno = 1
##while nroAlumno <= 40:
##    nombre = input("Ingrese nombre del alumno: ")
##    nota1  = int(input("Ingrese nota 1: "))
##    nota2  = int(input("Ingrese nota 2:"))
##    promedio = (nota1+nota2)/2
##    print("El promedio de {} es: {}".format(nombre,promedio))
##    nroAlumno = nroAlumno + 1
##print("Fin.")
##
##
######################################################################
### si quiero tenerlo mas flexible en cuanto a cuántos ingreso
##nroAlumno = 1
##nroAlumnos = int(input("Ingrese cuántos alumnos hay: "))
##while nroAlumno <= nroAlumnos:
##    nombre = input("Ingrese nombre del alumno: ")
##    nota1  = int(input("Ingrese nota 1: "))
##    nota2  = int(input("Ingrese nota 2:"))
##    promedio = (nota1+nota2)/2
##    print("El promedio de {} es: {}".format(nombre,promedio))
##    nroAlumno = nroAlumno + 1
##print("Fin.")
#####################################################################
#como hago si no se cuantos alumnos tengo de entrada
#opcion1: pregunto si sigue o si no
#opcion2: variable por ingreso de control ej nombre input == -1

###opcion3: ingreso algo absurdo en el argumento de comparación del while (0 en el nombre por ej)
##nroAlumno = 1
##nombre = input("Ingrese nombre del alumno: ")
##while nombre != "0":
##    nota1  = int(input("Ingrese nota 1: "))
##    nota2  = int(input("Ingrese nota 2:"))
##    promedio = (nota1+nota2)/2
##    print("El promedio de {} es: {}".format(nombre,promedio))
##    nroAlumno = nroAlumno + 1
##    nombre = input("Ingrese nombre del alumno: ")
##print("Fin.")

#####################################################################

###opcion1: variable por ingreso de control ej nombre input == -1
##
##nroAlumno = 1
##nombre = input("Ingrese nombre del alumno: ")
##while nombre != "0":
##    nota1  = int(input("Ingrese nota 1: "))
##    nota2  = int(input("Ingrese nota 2:"))
##    promedio = (nota1+nota2)/2
##    print("El promedio de {} es: {}".format(nombre,promedio))
##    nroAlumno = nroAlumno + 1
##    nombre = input("Ingrese nombre del alumno: ")
##print("Fin.")

#####################################################################

###opcion2: pregunto si sigue o si no
##
##nroAlumno = 1
##seguir = input("Ingresa alumnos? S/N: ")
##while seguir == "S":
##    nombre = input("Ingrese nombre del alumno: ")
##    nota1  = int(input("Ingrese nota 1: "))
##    nota2  = int(input("Ingrese nota 2:"))
##    promedio = (nota1+nota2)/2
##    print("El promedio de {} es: {}".format(nombre,promedio))
##    nroAlumno = nroAlumno + 1
##    seguir = input("Hay mas alumnos? S/N: ")
##print("Fin.")

#####################################################################

##gasto_total = 0
##semana = 1
##while semana < 5:
##    gasto = float(input(""))
##    gasto_total = gasto + gasto_total
##    semana = semana + 1
##promedio = gasto_total/4

#####################################################################

###estructura bien planteada:   if para procesar info. Con pregunta estilo seguir? no sería la estructura correcta
##numero = int(input(""))
##while numero != 0:
##
##
##    numero = int(input(""))

cantidad = 0
numero = int(input("Ingrese numero, 0 para terminar: "))
while numero != 0:
    if numero > 0:
        cantidad = cantidad + 1
    numero = int(input("Ingrese numero, 0 para terminar: "))
print("Cantidad de numeros positivos: {}".format(cantidad))
