pesoPayaso = 112
pesoMuneca = 75
numPayasos = int(input("Introduzca el número de payasos en el último envío: "))
numMunecas = int(input("Introduzca el número de muñecas en el último envío: "))
pesoTotal = numPayasos * pesoPayaso + numMunecas * pesoMuneca
print("El peso total del último envío será de: " + str(pesoTotal) + "g")