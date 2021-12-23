try:
    masa =  int(input("Introduce tu peso en Kg : "))
    altura = float(input("Introduce tu altura en Mts: "))
    if(type(masa)==int and type(altura)==float):
            total = (masa) / pow(altura,2)
            print("Tu índice de masa corporal es "+ str(round(total,2)))
except ValueError:
    print("Los valores deben ser numéricos")