
// Realiza un resta de cualquier numero sin usar el sigo ( - )
// 4 y 1, debe de ser igual a 3

let numero1 = parseInt(prompt("Ingresex numero1: "));
let numero2 = parseInt(prompt("Ingrese numero2: "));

let restador = 0;

if(numero1 > numero2){
  for(let i = numero2;i<numero1;i++){
    restador++;
  }
  console.log(restador)
}
else if(numero2 > numero1){
  for(let i = numero1;i<numero2;i++){
    restador++;
  }
  console.log(restador)
}
