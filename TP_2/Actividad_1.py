

""" Se solicita un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa
un monto negativo, no se debe procesar y se debe pedir que ingrese
un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta
que, si las ventas superan el monto total de 1000, se le debe aplicar un
10% de descuento. """

continua = 'S'
montoAcum = 0
while continua == 'S':
    montoVenta = float(input('Ingrese el monto de venta '))
    if montoVenta > 0:
        montoAcum = montoAcum + montoVenta
    elif montoVenta < 0:
        print('Monto no valido.')
    else:
        if montoAcum > 1000:
            print('El monto total a pagar es', montoAcum * 0.90)
            break
        else:
            print('El monto total a pagar es', montoAcum)
            break