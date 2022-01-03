def ejercicio_5(peso, estatura):
    """La funcion toma el peso y la estatura de una persona
       y calcula su IMC

    Args:
        peso (number): Peso de la persona en Kg
        estatura (number): Estatura de la persona en m
    """
    imc = peso/estatura
    print(f'Tu indice de masa corporal (IMC) es {imc}')
