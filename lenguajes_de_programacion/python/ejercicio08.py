precioBarraPan = 3.49
descuentoPanQueNoEsDelDia = 0.6
numBarras = int(input("Introduzca el número de barras de pan que no son del día: "))
descuentoBarrasDePan = round(descuentoPanQueNoEsDelDia * numBarras * precioBarraPan, 2)
costeFinalTotal = round(numBarras * precioBarraPan - descuentoBarrasDePan, 2)
print("Precio barra de pan: " + str(precioBarraPan))
print("Descuento por no ser fresca: " + str(descuentoBarrasDePan))
print("Coste final total: " + str(costeFinalTotal))