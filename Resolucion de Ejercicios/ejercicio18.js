// # Ejerccio 18

// Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte
// al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide
// con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas

let contraseña = 'holamundo';
let ingresarContraseña = prompt("Ingrese Contraseña: ");

if(ingresarContraseña === contraseña){
  alert("Contraseña acertada...!!");
}

