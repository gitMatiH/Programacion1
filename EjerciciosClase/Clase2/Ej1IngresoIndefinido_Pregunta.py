#opcion2: pregunto si sigue o si no

nroAlumno = 1
seguir = input("Ingresa alumnos? S/N: ")
while seguir == "S":
    nombre = input("Ingrese nombre del alumno: ")
    nota1  = int(input("Ingrese nota 1: "))
    nota2  = int(input("Ingrese nota 2:"))
    promedio = (nota1+nota2)/2
    print("El promedio de {} es: {}".format(nombre,promedio))
    nroAlumno = nroAlumno + 1
    seguir = input("Hay mas alumnos? S/N: ")
print("Fin.")
