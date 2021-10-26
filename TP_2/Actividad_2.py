

""" Se solicita un programa que permita al usuario ingresar una cantidad de
números positivos indefinida (la cantidad que ingresará no se conoce y
puede cambiar en cada ejecución), finalizando cuando ingresa el número
0 (que no se tendrá en cuenta). Una vez terminada la lectura de números,
informar cuál fue el mayor de losnúmeros ingresados. """

mayor = 0

while mayor >= 0:
    num = int(input('Ingrese un numero mayor a 0 '))
    if num > mayor:
        mayor = num
    elif num == 0:
        print('El mayor numero ingresado es ', mayor)
        break