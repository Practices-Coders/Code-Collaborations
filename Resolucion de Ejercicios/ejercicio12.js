// # Ejercicio 12

// Escribir un programa que pregunte el nombre completo del usuario en la consola y después
// muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas,
// otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
// El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera

let nombre = prompt("Ingrese Nombre: ");
//nombres y apellidos en minuscula
console.log(nombre.toLowerCase());
//nombres y apellidos en mayusculas
console.log(nombre.toUpperCase());
//caso 3: primera letra del nombre y de los apellidos en mayúscula.
let aux = nombre.split(" ")//de cadena lo convertimos a arreglo
let [a,...b] = aux;//destructuracion
let cadenaAux = '';//cadena vacia

for(let i=0;i<a.length;i++){
  if(i==0){
    cadenaAux += a[i].toUpperCase();//primera caracter en mayuscula
  }else{
    cadenaAux += a[i].toLowerCase();
  }
}

b = b.map(e => e.toUpperCase()).join(" ")//mayusculas apellidos

let cadena = cadenaAux.concat(" "); //cadena inicializada con cadenaAux donde se encuentra el valor de a filtrada.

console.log(cadena.concat(b))//concatenamos el nombre y apellidos



