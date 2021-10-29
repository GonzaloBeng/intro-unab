

""" Se solicita un programa que permita al usuario ingresar una cantidad de
números positivos indefinida (la cantidad que ingresará no se conoce y
puede cambiar en cada ejecución), finalizando cuando ingresa el número
0 (que no se tendrá en cuenta). Una vez terminada la lectura de números,
informar cuál fue el mayor de los números ingresados. """

mayor = 0
totalValores = 0
totalPares = 0
totalImpares = 0

while mayor >= 0:
    num = int(input('Ingrese un numero ')) 
    if num > mayor:
        mayor = num
    elif num < 0:
        print('Ingrese solo numeros positivos')
    elif num == 0:
        break
    if num % 2 == 0:
        totalPares = totalPares + 1    
    else:
        totalImpares = totalImpares + 1
    totalValores = totalValores + 1
print('El mayor numero ingresado es ', mayor)
print('La cantidad de valores ingresados es ', totalValores)
print('La cantidad de numeros pares es de ', totalPares, 'y de impares', totalImpares)