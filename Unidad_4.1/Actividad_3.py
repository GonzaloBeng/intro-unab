

""" Consigna: Escribir un programa que solicite por teclado 10 notas de alumnos y
nos informe cuántos tienen notas mayores o iguales a 7 y cuántos
menores. """

contador = 0
contAprob = 0
contDesAprob = 0

for contador in range(10):
    nota = int(input('Ingrese la nota '))
    if nota >= 7:
        contAprob = contAprob + 1
    else:
        contDesAprob = contDesAprob + 1

print(f'La cantidad de alumnos con notas mayores o igual a 7 son {contAprob} y con nota menor a 7 son {contDesAprob}')