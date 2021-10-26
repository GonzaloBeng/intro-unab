

""" Consigna: se realiza una encuesta entre 100 personas que votan por los
candidatos A o B (solo este dato se ingresa).
Se pide: calcular y mostrar los porcentajes obtenidos por los dos candidatos. """

encuestados = 0
candA = 0
candB = 0

""" while encuestados < 100:
    opcion = input('''\n Que candidato va a votar? Ingresa el numero correspondiente
    1. Candidato A
    2. Candidato B
    ''')
    if opcion == '1':
        encuestados = encuestados + 1
        candA = candA + 1
    elif opcion == '2':
        encuestados = encuestados + 1
        candB = candB + 1
    else:
        print('Ingrese una opcion valida')


print('El porcentaje del candidato A es de ', int(((candA*100)/encuestados)),'%')
print('El porcentaje del candidato B es de ', int(((candB*100)/encuestados)),'%')"""



for encuestados in range(0,100):
    opcion = input('''\n Que candidato va a votar? Ingresa el numero correspondiente
    1. Candidato A
    2. Candidato B
    ''')
    if opcion == '1':
        candA = candA + 1
    elif opcion == '2':
        candB = candB + 1
    else:
        print('Ingrese una opcion valida') 

print('El porcentaje del candidato A es de ', int(((candA*100)/100)),'%')
print('El porcentaje del candidato B es de ', int(((candB*100)/100)),'%')