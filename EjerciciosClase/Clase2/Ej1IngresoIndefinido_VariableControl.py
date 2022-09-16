#opcion1: variable por ingreso de control ej nombre input == -1
#ingreso algo absurdo en el argumento de comparación del while
#(0 en el nombre por ej)

nroAlumno = 1
nombre = input("Ingrese nombre del alumno: ")
while nombre != "0":
    nota1  = int(input("Ingrese nota 1: "))
    nota2  = int(input("Ingrese nota 2:"))
    promedio = (nota1+nota2)/2
    print("El promedio de {} es: {}".format(nombre,promedio))
    nroAlumno = nroAlumno + 1
    nombre = input("Ingrese nombre del alumno: ")
print("Fin.")
