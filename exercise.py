"""
ejercicio 1

Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
"""
print("¡Hola Mundo!")

"""
ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable
"""
h = "¡Hola Mundo!"
print(h)

"""
ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla
la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""
#La función input() permite a los usuarios introducir datos de distintos tipos desde la entrada estándar
usuario = input('Cuál es su nombre?. ')
print(f'Hola {usuario}')

"""
ejercicio 4
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""
#Hacemos una validacion si el usuario ingresa un valor no numerico
while True:
    try:
        hrs = float(input('Ingrese el numero de Horas trabajadas: '))
        cst = float(input('Ingrese el coste por Horas: '))
        total = hrs*cst
        print(f'El total a pagar es: {total}')
        break
    except ValueError:
        print('Error!: Ingrese solo valores numericos.')

