/*first npm install readline-sync*/
var readline = require('readline-sync');
let masa = readline.questionInt("Introduce tu peso en Kg : ");
let altura = readline.questionFloat("Introduce tu altura en Mts: ");

if (typeof masa == 'number' && typeof altura == 'number') {
    let total = masa / Math.pow(altura, 2);
    console.log('Tu índice de masa corporal es ' + total.toFixed(2));
}