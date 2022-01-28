"""
# Ejercicio 5

---
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice
de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal
es < imc> donde < imc> es el índice de masa corporal calculado redondeado con dos decimales

"""
# inicio del programa
print('Bienvenido a calculador de IMC')

# Solicitar los datos
peso = float(input('Ingrese su peso en kg: '))
estatura = float(input('Ingrese su estatura en m: '))

# Realizar los calculos
calc = peso / ( estatura ** 2) # se usa la funcion de ** para potencias

# imprimir los datos
print(f"El IMC es {calc}")

#fin del programa
