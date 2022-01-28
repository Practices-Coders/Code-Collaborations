"""
# Ejercicio 4
---
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde

"""
# inicio del programa
print("Bienvenido...")
# solicitar las horas ya que se usa input pero parsearlo a tipo flotante 
horas = float(input("ingresa el numero de horas trabajadas: "))
# solicitar el coste por hora pero el metodo es el mismo que las horas
salario = float(input("Ingresa el coste por hora: "))

# calculo
pago = horas * salario

# imprimir los resultados
print(f"El pago: ${pago}")