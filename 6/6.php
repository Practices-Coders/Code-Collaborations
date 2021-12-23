<?php
$payasos =  readline("Introduce numero de payasos: ");
$munecas = readline("Introduce numero de muñecas: ");
define('PESO_PAYASO',0.112);
define('PESO_MUNECA',0.075);

if(is_numeric($payasos) && is_numeric($munecas)){
    
    $total = (intval($payasos) * PESO_PAYASO) + (intval($munecas) * PESO_MUNECA);
    $total = floatval($total);
    echo "El peso total del paquete enviado sera en Kg: ".round($total,2);
}else{
    echo "Los valores deben ser numéricos";
}