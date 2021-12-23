/*first npm install readline-sync*/
var readline = require('readline-sync');

let payasos = readline.questionInt("Introduce numero de payasos: ");
let munecas = readline.questionInt("Introduce numero de muniecas: ");
const peso_payaso = 0.112;
const peso_muneca = 0.075;
if (typeof payasos == 'number' && typeof munecas == 'number') {
    let total = (payasos * peso_payaso) + (munecas * peso_muneca);
    console.log(`El peso total del paquete enviado sera en Kg: ${ total.toFixed(2) }`);
}