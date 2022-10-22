#Ej1
nroAlumno = 1
while nroAlumno <= 40:
    nombre = input("Ingrese nombre del alumno: ")
    nota1  = int(input("Ingrese nota 1: "))
    nota2  = int(input("Ingrese nota 2:"))
    promedio = (nota1+nota2)/2
    print("El promedio de {} es: {}".format(nombre,promedio))
    nroAlumno = nroAlumno + 1
print("Fin.")
