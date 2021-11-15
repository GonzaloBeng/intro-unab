

""" Consigna: en un campeonato intercolegial, donde participan 50 alumnos, se desea conocer la cantidad de alumnos anotados por categoría. 
Por cada uno, se ingresa el nombre y la edad. Las categorías son las siguientes:
~ INFANTIL, para los menores de 11 años
~ PUBER, entre los 11 y los 14 años
~ JUVENIL, para los mayores de 14 años """


contador = 0
juvenil = 0
puber = 0
infantil = 0
mayor = 0
menor = 0
edadAcum = 0

for contador in range(3):
    nombre = input('Ingrese su nombre: ')
    edad = int(input('Ingrese la edad del alumno: '))
    if edad > 14:
        juvenil = juvenil + 1
    elif edad > 11 and edad <= 14:
        puber = puber + 1
    else:
        infantil = infantil + 1
    if edad > mayor:
        mayor = edad
    if menor == 0:
        menor = edad
    elif edad < menor:
        menor = edad

    edadAcum = edadAcum + edad
    contador = contador + 1

print(f'La cantidad de alumnos en la categoria juvenil es {juvenil}, en puber es {puber} y en infantil {infantil}.')
print(f'La edad mas alta de los alumnos es de {mayor} y la mas baja es {menor}')
print(f'El promedio de todas las edades es de {edadAcum/contador}')
