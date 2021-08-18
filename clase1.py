## Ejercicios clase 17/08

## 1) Sabiendo la cantidad de horas que trabaja un obrero al mes y el valor horario, imprimir cuál es su sueldo a fin de mes. 

horas_trabajadas = 120;
valor_hora = 250;
sueldo = horas_trabajadas*valor_hora;

print('El sueldo del obrero a fin de mes es:','$',sueldo);

## 2) Diseñar un algoritmo que a partir de un número ingresado, calcule y muestre:

numero = 100;

print('La mitad es:', numero/2);
print('Su raiz cuadrada:',);
print('Su raiz cubica:');

## 3) Dado la cantidad de votos obtenidos por 3 partidos distintos, calcular los porcentajes de votos alcanzados por cada partido

partido1 = 200;
partido2 = 300;
partido3 = 500;
votos_totales = partido1 + partido2 + partido3;

porcentaje_partido1 = (partido1/votos_totales*100);
porcentaje_partido2 = (partido2/votos_totales*100);
porcentaje_partido3 = (partido3/votos_totales*100);

print('El partido1 saco un:',porcentaje_partido1,'%');
print('El partido2 saco un:',porcentaje_partido2,'%');
print('El partido3 saco un:',porcentaje_partido3,'%');

## 4) Obtenga el importe de un viaje en remis, sabiendo que el valor del km. es de $54.00. Se debe ingresar los kms. de cada viaje

kms_viajados = 10;
valor_km = 54;
importe = kms_viajados * valor_km;

print('El importe de su viaje es de $',importe);

## 5) Calcular el interés ingresando los siguientes datos: Capital, Razón, Tiempo y Unidad de Tiempo. Calcular el interés y volcarlos por pantalla

capital = 200;
razon = 100;
tiempo = 60;
unidad_tiempo = 20;
interes = (capital*razon*tiempo)/(100*unidad_tiempo);

print(interes);

##6) Escribir un algoritmo que convierta las horas ingresadas en minutos y en segundos, y las muestre por pantalla

horas = 2;
minutos = horas*60;
segundos = horas*3600;
print(horas,'equivalen a',minutos,'minutos o', segundos, 'segundos');

##7) Escribir un algoritmo que convierta los valores ingresados en cms. a pulgadas. Recordar que una pulgada equivale a 2.5 cm

cms = 100;
pulgadas = cms/2.5

print(cms, 'cms equivalen a',pulgadas,'pulgadas');

## Dada una cantidad en pesos, obtener la equivalencia en dólares, asumiendo que la unidad cambiaria es un dato desconocido, que varía minuto a minuto.
cantidad_pesos = 1000;
unidad_cambiaria = ;
cantidad_dolares = cantidad_pesos / unidad_cambiaria

print(cantidad_pesos,'equivalen a',cantidad_dolares,'dolares')