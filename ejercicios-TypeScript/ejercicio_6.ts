const ejercicio_6 = (n_payasos: number, n_munecas: number): void => {
  /**
   * La funcion toma como parametro el numero de payasos y el
   * numero de moñecas a vender y calcula el peso total del paquete.
   *
   * Args:
   *  n_payasos (number): numero de payasos
   *  n_munecas (number): numero de muñecas
   */

  console.log(
    `El peso total del paquete es ${n_payasos * 112 + n_munecas * 75}g`
  );
};

ejercicio_6(2, 1);
