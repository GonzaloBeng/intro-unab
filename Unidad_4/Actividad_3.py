

""" Consigna: realizar un programa que calcule el total a pagar por la compra de camisas.
Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra,
y si son menos de tres camisas un descuento del 10%. El precio de cada camisa se ingresa junto a la cantidad de camisas vendidas.  """

cantCamisas = int(input('Ingrese la cantidad de camisas compradas '))
precioCamisas = int(input('Ingrese el valor de las camisas '))


if cantCamisas >= 3:
    precioTotal = precioCamisas * cantCamisas
    precioFinal = precioTotal * 0.80
else:
    precioTotal = precioCamisas * cantCamisas
    precioFinal = precioTotal * 0.90

print('El importe a pagar es de ', precioFinal)