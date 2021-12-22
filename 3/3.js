/*first npm install readline-sync*/
var readline = require('readline-sync');
let nombre = readline.question("Escribe tu nombre: ");
console.log("¡Hola " + nombre + "!");