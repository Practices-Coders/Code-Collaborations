<?php
$horas = readline("Introduce numero de horas trabajadas: ");
$costo = readline("Introduce costo por horas: ");

if(is_numeric($horas) && is_numeric($costo)){
    $total = intval($horas) * floatval($costo);
    echo "El total del pago $ ".round($total,2);
}else{
    echo "Los valores deben ser numéricos";
}
