// Realizar un programa que indique si una palabra es capicúa ejemplo: oso, radar, oro, solos

let palabra = prompt("Ingrese palabra: ");
let capicua = (palabra === palabra.split("").reverse().join(""))?'si son capicuas':'no es capicua';

console.log(capicua);




