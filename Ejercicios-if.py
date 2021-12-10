# Crear un programa que tenga dos variables y defina cual es el mayor
# y cual es el menor

valor1: int = 19
valor2: int = 100

if valor1 > valor2:
    print(valor1, "Es mayor que", valor2)
elif valor1 < valor2:
    print(valor2, "Es mayor que", valor1)
else:
    print(valor1, "es igual a", valor2)
    
#Crear un programa que tome tres números como argumentos
# y devuelva el mayor de ellos.

numero1:int = 100
numero2:int = 100
numero3:int = 90

if numero1 > numero2 and numero1 > numero3:
    print(numero1,"es  mayor a",numero2,numero3)
elif numero1 == numero2 and numero1 > numero3:
    print(numero1 ,"es igual a",numero2,"y mayor a ",numero3)
elif numero1 == numero3 and numero1 > numero2:
    print(numero1, "es igual a", numero3, "y mayor a ", numero2)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2,"es mayor a",numero1,numero3)
elif numero2 == numero1 and numero2 > numero3:
    print(numero2 ,"es igual a",numero1,"y mayor a ",numero3)
elif numero2 == numero3 and numero2 > numero1:
    print(numero2, "es igual a", numero3, "y mayor a ", numero1)
elif numero3 > numero1 and numero3 > numero2:
    print(numero3,"es mayor a",numero1,numero2)
else:
    print("Los tres valores son iguales")
