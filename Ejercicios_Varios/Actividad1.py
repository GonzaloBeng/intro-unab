
## 1) Se intenta preparar budines de pan. Los ingredientes para 4 personas de la receta son los indicados en el cuadro adjunto.
## Realizar un algoritmo que calcule los ingredientes para un número variable de personas que se lee por teclado.

receta = 'continua'

while receta == 'continua':
    panes = 2
    huevos = 3
    azucar = 0.5
    agua = 1
    personas = int(input('Ingresar la cantidad de personas para su receta '))
    print('Para tu receta de budin de pan necesitas: ')
    print(((panes * personas)/4), 'panes con cascara')
    print(((huevos * personas)/4), 'huevos batidos')
    print(((azucar * personas)/4), 'kilo de azucar')
    print(((agua * personas)/4), 'tazas de agua')