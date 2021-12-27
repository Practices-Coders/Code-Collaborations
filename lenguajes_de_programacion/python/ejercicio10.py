def calcularPrecioConIva(precio, iva=0.21):
    return precio * (1 + iva)

precioSinIva1 = float(input("Introduzca el precio sin IVA: "))
precioConIva1 = calcularPrecioConIva(precioSinIva1)
print("Precio con IVA del 21%: " + str(precioConIva1))

precioSinIva2 = float(input("Introduzca el precio sin IVA: "))
iva = float(input("Introduzca el IVA en %: "))
precioConIva2 = calcularPrecioConIva(precioSinIva2, iva/100)
print("Precio con IVA del " + str(iva) + "%: " + str(precioConIva2))