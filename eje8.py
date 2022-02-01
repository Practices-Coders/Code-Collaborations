"""
# Ejercicio 8


---

Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento 
del 60%.Escribir un programa que comience leyendo el número de barras vendidas que no son del 
día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que
se le hace por no ser fresca y el coste final total
"""
# inicio del programa
print("Bienvenido...")
# Declaracion de la variable constante
costo = 3.49
# solicitud de la cantidad de pan
cantidad = int(input("Ingrese la cantidad de panes: "))

# elaboracion de los calculos
Coste_neto = costo * cantidad # se multiplica la cantidad por el precio
descuento = Coste_neto * 0.6 # se multiplica por 0.6 para conocer el descuento
total = Coste_neto - descuento # Una resta para obtener el total del costo 

# imprimir los datos
print(f"""
Cantidad: {cantidad} pzs
costo neto: {costo} € 
costo total: {Coste_neto} €
Descuento: -{descuento}€
Total: {total}€.
""")