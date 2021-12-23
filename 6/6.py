try:
    payasos =  int(input("Introduce numero de payasos: "))
    munecas = float(input("Introduce numero de muñecas: "))
    PESO_PAYASO = 0.112
    PESO_MUNECA = 0.075
    if(type(payasos)==int and type(munecas)==float):
            total = (payasos * PESO_PAYASO) + (munecas * PESO_MUNECA)
            print("El peso total del paquete enviado sera en Kg: " + str(round(total,2)))
except ValueError:
    print("Los valores deben ser numéricos")