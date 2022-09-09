#Ej4
'''
Al terminar un día en un colegio secundario se hace una estadística de faltas
sabiendo de cada curso:

-Curso(1-5)
-Presentes
-Ausentes

Calcular:

-Por cada curso el porcentaje de presentes sobre el total
-Cantidad de ausentes en el colegio
-Curso con mayor cantidad de ausentes

'''

# Sabemos, o sea tenemos como datos:
# Números de cursos son los elementos iésimos de las listas
# de presentes y ausentes.

#Ej curso 1 está en la posición cero. Curso 5 está en la posición cuatro.
CantAlumnos = [30, 20, 25, 23, 22]
Presentes = [26, 19, 22, 19, 20]
Ausentes = [
    CantAlumnos[0]-Presentes[0],
    CantAlumnos[1]-Presentes[1],
    CantAlumnos[2]-Presentes[2],
    CantAlumnos[3]-Presentes[3],
    CantAlumnos[4]-Presentes[4]
    ]
print("Datos:")
print("CantAlumnos: ", CantAlumnos,"\nPresentes: ", Presentes,"\nAusentes: ", Ausentes,"\n")

### por cada curso el porcentaje de presentes sobre el total
# calculo total_presentes
total_presentes = 0
i=0
while i < len(CantAlumnos):
    total_presentes = total_presentes + int(Presentes[i])
    i = i+1
print("Total de alumnos presentes: {}".format(total_presentes))

## calculo porcentaje de presentismo por cursos
PresentismoPorCurso = []
for i in range(0, len(CantAlumnos)): PresentismoPorCurso.append(int((Presentes[i]*100)/CantAlumnos[i])) # redondea a entero
print("Porcentaje de presentismo por curso: ", PresentismoPorCurso)

# calculo cuántos alumnos tiene el colegio
total_alumnado = 0
for i in range(0, len(CantAlumnos)): total_alumnado = total_alumnado + CantAlumnos[i]
print("Total alumnado: ", total_alumnado)

##calculo porcentaje de presentismo total del colegio
presentismo_colegio = 0
for i in range(0, len(CantAlumnos)): presentismo_colegio = presentismo_colegio + Presentes[i]
porcentaje_presentismo_colegio = (presentismo_colegio*100)/total_alumnado
print("Porcentaje de presentismo en el colegio: {}".format(int(porcentaje_presentismo_colegio)))

##radio de presentismo por cursos
RadioPresentismoPorCurso = []
for i in range(0, len(CantAlumnos)): RadioPresentismoPorCurso.append(round(int(PresentismoPorCurso[i])/int(porcentaje_presentismo_colegio), 2))
print("Radio presentismo_curso_porcentual:presentismo_total_porcentual es ", RadioPresentismoPorCurso)

###
print()
###

### cantidad de ausentes en el colegio
total_ausentes = 0
for i in range(0, len(CantAlumnos)): total_ausentes = total_ausentes + Ausentes[i]
print("Total de ausentes: ", total_ausentes)

### curso con mayor cantidad de ausentes
curso_mayor_ausentismo = 0
for i in range(0, len(Ausentes)):
    if (
    Ausentes[i] > Ausentes[curso_mayor_ausentismo] and
    RadioPresentismoPorCurso[i]<RadioPresentismoPorCurso[curso_mayor_ausentismo]
    ):
    # de todas formas si los dos son iguales, toma el primero por defecto; habría que implementar
    # una lógica adicional para poner una lista con todos los menores, y se actualizaria y borraria
    # y agregaria elementos dinámicamente
        curso_mayor_ausentismo = i
print("El curso con mayor ausentismo es el número {}, que corresponde "
      "a la posición {} de la lista CantAlumnos".format(curso_mayor_ausentismo+1, curso_mayor_ausentismo))
