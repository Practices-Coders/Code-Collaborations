const ejercicio_5 = (peso: number, estatura: number): void => {
  /**
   * La funcion toma el peso y la estatura de una persona
   * calcula su IMC.
   *
   * Args:
   *  peso (number): Peso de la persona en Kg
   *  estatura (number): El estatura de la persona en m
   */

  let imc: number = peso / estatura;
  console.log(`Tu indice de masa corporal es ${imc}`);
};
