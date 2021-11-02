

""" Consigna: Desarrollar un programa que permita la carga de 10 valores
por teclado y nos muestre posteriormente la suma de los valores
ingresados y su promedio."""

contador = 0
numAcum = 0

for contador in range(10):
    num = float(input('Ingrese un numero: '))
    numAcum = numAcum + num
    contador = contador + 1

print(f'La suma de los valores da {numAcum} y su promedio {numAcum/contador}')