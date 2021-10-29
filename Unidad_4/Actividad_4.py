

""" Consigna: En una fábrica de construcción se ingresan de sus empleados los
siguientes datos (no se sabe cuántos empleados hay): 
Apellido y nombre, edad, sexo, ysueldo.
Se pide:
a) Imprimir el apellido y nombre de todas las mujeres que ganen más de $1000.
b) Aumentar un 25% el sueldo de todos los empleados del sexo masculino, y
mostrar por pantalla el apellido y nombre, y el nuevo sueldo.
c) Imprimir el promedio de edades de los hombres y el promedio de edades de
las mujeres.  """

continua = 'S'
promMuj = 0
promHom = 0
contMuj = 0
contHom = 0

while continua == 'S':
    nombreApellido = input('Ingrese su Nombre y Apellido ')
    edad = int(input('Ingrese su edad '))
    sexo = input('''\n Cual es su sexo? Ingrese el numero correspondiente
        1. Femenino
        2. Masculino
        ''')
    sueldo = int(input('Ingrese su sueldo actual '))
    if sexo == '1':
        contMuj = contMuj + 1
        promMuj = promMuj + edad
        if sueldo > 1000:
            print(nombreApellido, 'es mujer y gana mas de 1000')
    elif sexo == '2':
        contHom = contHom + 1
        promHom = promHom + edad
        print(nombreApellido,'su nuevo sueldo con aumento es de: ',(sueldo + sueldo * 0.25))
    else:
        print('Hubo un error en el ingreso de datos')
    if (contMuj > 0):
        print('El promedio de edad femenino es de ', promMuj/contMuj, 'años')
        print('El promedio de edad masculino es de 0 años')
    elif contHom > 0:
        print('El promedio de edad femenino es de ', promHom/contHom, 'años')
        print('El promedio de edad femenino es de 0 años')
