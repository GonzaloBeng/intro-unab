

""" Consigna: una persona enferma, que pesa 70 kg, se encuentra en reposo y
desea saber cuántas calorías consume su cuerpo durante todo el tiempo que realiza una
misma actividad. Las actividades que tiene permitido realizar son únicamente dormir o estar
sentado en reposo. Los datos que tiene son que estando dormido consume 1.08 calorías por minuto y
estando sentado en reposo consume 1.66 calorías por minuto. Serán datos de entrada: la
actividad y el tiempo expresado en minutos. """

actividad =  input('''\n Que tipo de actividad quiere calcular? Ingresa el numero correspondiente
    1. Dormir
    2. Sentarse
    ''')

if actividad == '1':
    tiempo = int(input('Ingrese la cantidad de minutos que realizara la actividad '))
    print('Las calorias consumidas son de: ', (tiempo * 1.08))
elif actividad == '2':
    tiempo = int(input('Ingrese la cantidad de minutos que realizara la actividad '))
    print('Las calorias consumidas son de: ', (tiempo * 1.66))
else:
    print('Ingrese una opcion valida')