// Realizar un programa que solicite numeros hazta que se introduzca un cero debe imprimir la suma y el promedio de todos los numeros introducidos

let suma = 0;

while (true) {
  let numero = parseInt(prompt("Ingrese"));
  if(numero === 0){
    break;
  }
  suma += numero;
}

console.log(suma)

