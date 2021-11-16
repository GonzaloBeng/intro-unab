
'''INTEGRANTES:
Bengoechea, Gonzalo 38.254.089
Pedrol, Santiago 44.650.233
Prieto, Julian 45.065.709
Reynoso, Octavio 41.211.111
Torres, Paula Florencia''' 

'''En una librería, para llevar a cabo su inventario físico, se van ingresando de cada
libro, los siguientes datos: Título del libro, Autor, Tema, y cantidad de páginas. Se
comenzarán con los primeros 20 libros.
Se pide calcular y mostrar:
La cantidad de libros ingresados por tema, tomando en cuenta, que solo existen
3(tres) temas. Ellos son: Filosofía, Historia y Literatura.
 El título y autor del libro con mayor cantidad de páginas.
 El promedio de páginas por libro.
 El titulo y cantidad de páginas del libro con menor cantidad de páginas
 El promedio de libros por temas ( promedio de Filosofía, Historia y Literatura)'''

#Inicio

# Defino la funcion
def libros():
    #Defino las variables a usar
    contFilosofia = 0
    contHistoria = 0
    contLiteratura = 0
    contadorTotal = 0
    mayorPaginas = 0
    mayorTitulo = ''
    mayorAutor = ''
    menorTitulo = ''
    menorPaginas = 0
    acumPaginas = 0

    for i in range(20):
        titulo = input('Ingrese el titulo del libro: ')
        autor = input('Ingrese el Autor del libro: ')
        tema = input(''' Ingrese el tema del libro:
                1. Filosofia
                2. Historia
                3. Literatura
                ''')
        paginas = int(input('Ingrese la cantidad de paginas: '))

        #Consulto el tema del libro
        if tema == '1':
            contFilosofia += 1
            contadorTotal +=1
        elif tema == '2':
            contHistoria +=1
            contadorTotal +=1
        elif tema == '3':
            contLiteratura += 1
            contadorTotal +=1
        else:
            print('Ingrese un tema valido.')

        #Determino el libro con mayor y menor paginas
        if mayorPaginas < paginas:
            mayorPaginas = paginas
            mayorTitulo = titulo
            mayorAutor = autor
        if menorPaginas == 0:
            menorTitulo = titulo
            menorPaginas = paginas
        elif menorPaginas > paginas:
            menorTitulo = titulo
            menorPaginas = paginas
        acumPaginas += paginas

    #Muestro por pantalla
    print(f'''La cantidad de libros ingresados es de: 
            {contFilosofia} libro/s de Filosofia,
            {contHistoria} libro/s de Historia,
            y {contLiteratura} libro/s de Literatura.''')

    print(f'''El promedio de libros correspondiente es de: 
            Filosofia: {(contFilosofia*100)/contadorTotal}%
            Historia: {(contHistoria*100)/contadorTotal}%
            Literatura: {(contLiteratura*100)/contadorTotal}%.''')
    
    print(f'''{mayorTitulo} de {mayorAutor} es el libro con mas paginas: {mayorPaginas}''')
    print(f'''{menorTitulo} es el libro con menos paginas: {menorPaginas}''')
    print(f'''El promedio de paginas por libro es de {acumPaginas/contadorTotal}''')


#Llamo a la funcion
libros()

# Fin