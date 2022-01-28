"""
# Ejercicio 6

---
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y
la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas
que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número
de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

"""
# inicio del programa
# se definen los datos de los pesos de los dos jugetes
peso_payaso = 112
peso_mune = 75

# Solicitar los datos
payaso = int(input('Ingrese la cantidad de payasos: '))
munieca = int(input('Ingrese la cantidad de muñecas: '))

# area de calculo
peso_caja = (peso_payaso * payaso) + (peso_mune * peso_mune)

# imprimir los resultados
print(f"""
Cantidad de muñecas: {munieca}.

Peso en total.........{peso_caja} g
""")
# fin del programa