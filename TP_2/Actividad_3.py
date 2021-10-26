

""" Se solicita un programa que pregunte al usuario si desea analizar calificaciones de
alumnos y, sólo si responde “S” comenzaráel procesamiento de los datos, hasta que el
usuario ingrese algo diferente de “S”. Por cada alumno, permitir ingresar su
calificación. Si es mayor o igual a 4 el alumno está aprobado. Finalmente, mostrar
“Porcentaje de alumnos aprobados: x %” (donde x es el porcentaje de aprobados
sobre el total de calificaciones procesadas). También se debe imprimir “Promedio de los
aprobados: y” (donde y es la calificación promedio, sólo de los alumnos aprobados). """

opcion = str(input('Analizar calificaciones? S para si: '))
alumAprob = 0
contador = 0
acumNotas = 0
promAprob = 0

while opcion == 'S':
    nota = int(input('Calificacion del alumno: '))
    if nota >= 4:
            acumNotas = acumNotas + nota
            alumAprob = alumAprob + 1
            promAprob = promAprob + 1
    contador = contador + 1
    opcion = input('Continuar? S para si: ')
print('Porcentaje de alumnos aprobados: ', (alumAprob*100)/contador)
print('Promedio de los alumnos aprobados: ', (acumNotas/promAprob))