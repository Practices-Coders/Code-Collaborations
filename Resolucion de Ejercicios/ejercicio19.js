// # Ejercicio 19

// Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o 

let edad = parseInt(prompt("Ingrese edad: "));
let ingresos = parseInt(prompt("Ingrese ingresos mensuales: "));

if(edad > 16 && ingresos > 1000){
  console.log("Ud puede tributar..!!");
}else{
  console.log("No puede tributar..!!");
}








