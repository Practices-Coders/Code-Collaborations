"""
# Ejercicio 7


---

magina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido
a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un
programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después
el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales
"""
# inicio del programa
print("Bienvenido.")

# solicitar los datos
cantidad = float(input('Ingresar a cantidad inicial: $'))
cant_year = int(input("Cantidad de años a ahorrar: "))
# hacer los calculos
for i in range(cant_year): # se hace un for para los años ingresados
    cantidad = cantidad + (cantidad * 0.04) # sacar el interes total del año
    print(f"Cantidad de ahorro: ${round(cantidad,2)}") # mandar imprimir
                                                  # se usa la funcion round()

# fin del programa
