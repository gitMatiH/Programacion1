# si quiero tenerlo mas flexible en cuanto a cuántos ingreso
nroAlumno = 1
nroAlumnos = int(input("Ingrese cuántos alumnos hay: "))
while nroAlumno <= nroAlumnos:
    nombre = input("Ingrese nombre del alumno: ")
    nota1  = int(input("Ingrese nota 1: "))
    nota2  = int(input("Ingrese nota 2:"))
    promedio = (nota1+nota2)/2
    print("El promedio de {} es: {}".format(nombre,promedio))
    nroAlumno = nroAlumno + 1
print("Fin.")
