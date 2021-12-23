/*first npm install readline-sync*/
var readline = require('readline-sync');
let horas = readline.questionInt("Introduce numero de horas trabajadas: ");
let costo = readline.questionFloat("Introduce costo por horas: ");

if (typeof horas == 'number' && typeof costo == 'number') {
    let total = horas * costo;
    console.log('El total del pago $ ' + total.toFixed(2));
}