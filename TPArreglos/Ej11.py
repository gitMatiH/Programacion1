'''
Se dan 20 valores correspondientes a las estaturas de los alumnos
de un curso A y 20 de un curso B. Hallar:
a. Estatura máxima del curso A y del curso B y
    el lugar que ocupa alumno en la lista.
b. Comparar ambas estaturas e indicar cuál es
    la mayor imprimiendo un mensaje.
'''
import random

curso_a = []
j = 20
for i in range(0,j):
    curso_a.append(round(random.uniform(100.0, 240.0),2))
print("Lista a de: ", len(curso_a),"alumnos")
print("La lista a:")
print(curso_a)


curso_b = []
j = 20
for i in range(0,j):
    curso_b.append(round(random.uniform(100.0, 240.0),2))
print("Lista b de: ", len(curso_b),"alumnos")
print("La lista b:")
print(curso_b)


altura_max_a = curso_a[0]
pos_a = 1
altura_max_b = curso_b[0]
pos_b = 1
for i in range(0, j):
    if altura_max_a < curso_a[i]:
        altura_max_a = curso_a[i]
        pos_a = i+1

    if altura_max_b < curso_b[i]:
        altura_max_b = curso_b[i]
        pos_b = i+1

print()
print("El alumno mas alto del curso a mide: ", altura_max_a, "cm")
print("y su posición en la lista a fue: ", pos_a)

print()
print("El alumno mas alto del curso b mide: ", altura_max_b, "cm")
print("y su posición en la lista a fue: ", pos_b)

print()
if altura_max_a > altura_max_b:
    print("El alumno más alto pertenece al curso 'a'")
elif altura_max_a < altura_max_b:
    print("El alumno más alto pertenece al curso 'b'")
else:
    print("Los alumnos más altos del curso 'a' y 'b' son igual de altos.")
