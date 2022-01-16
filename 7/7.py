try:
    ahorros = float(input("Introduce la cantidad de ahorros en dolares: ($) "))
    if(type(ahorros) == float):
        for i in range(1,4):
            total = 0
            total = ahorros + (ahorros *0.3) * i   
            print("El total de ahorros tras el " + str(i) +".° año " + str(round(total,2)))   
           
except ValueError:
    print("Los valores deben ser numéricos")