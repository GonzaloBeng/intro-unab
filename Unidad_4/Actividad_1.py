
""" Consigna: Ingresar el sueldo y la antigüedad de un empleado. 
Aumentar su sueldo un 10%, siempre y cuando la antigüedad sea mayor a 7 años. 
Mostrar el sueldo aumentado.  """

sueldoActual = int(input('Ingrese sueldo actual del empleado '))
antiguedad = int(input('Ingrese la antigüedad del empleado '))

if antiguedad > 7:
    print('El nuevo sueldo del empleado es de: ', (sueldoActual + sueldoActual * 0.10))
else:
    print('El empleado no recibe aumento, su sueldo es de: ', sueldoActual )