
try:
    horas = int(input("Introduce numero de horas trabajadas: "))
    costo = float(input("Introduce costo por horas: "))    
    if(type(horas)==int and type(costo)==float):
        total = horas * costo
        print("El total del pago $ "+ str(round(total,2)))
except ValueError:
    print("Los valores deben ser numéricos")    