## A partir de una encuesta realizada a estudiantes de distintas universidades se pretende obtener algunas estadísticas. 
## Se ingresan:Cantidad de alumnos de Universidad Pública y Cantidad de alumnos de Universidad Privada 
## Calcular : Cantidad total de alumnos y Porcentaje de alumnos de universidad pública y privada. 

contador = 0
alumnosPublica = 0
alumnosPrivada = 0

while (True):
    opcion = input('''\n Que tipo de Universidad concurres? Ingresa una opcion
    1. Universidad publica
    2. Universidad Privada
    ''')
    if opcion == '1':
        contador = contador + 1
        alumnosPublica = alumnosPublica + 1
        print('La cantidad total de alumnos es de ', contador, 'alumnos')
        print('El porcentaje de alumnos de Univ. Publica es de ', int(((alumnosPublica*100)/contador)),'%')
        print('El porcentaje de alumnos de Univ. Privada es de ', int(((alumnosPrivada*100)/contador)),'%')
    elif opcion == '2':
        contador = contador + 1
        alumnosPrivada = alumnosPrivada + 1
        print('La cantidad total de alumnos es de ', contador)
        print('El porcentaje de alumnos de Univ. Publica es de ', int(((alumnosPublica*100)/contador)),'%')
        print('El porcentaje de alumnos de Univ. Privada es de ', int(((alumnosPrivada*100)/contador)),'%')
    else:
        print('Ingrese una opcion valida')