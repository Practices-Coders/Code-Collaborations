/*first npm install readline-sync*/
var readline = require('readline-sync')

let ahorros = readline.questionFloat("Introduce la cantidad de ahorros en dolares: ($) ");
if (typeof ahorros == 'number') {
    for (let i = 1; i <= 3; i++) {
        let total = ahorros + (ahorros * 0.3) * i;
        console.log("El total de ahorros tras el " + i + ".° año " + total.toFixed(2))
    }
}