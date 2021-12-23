<?php
$masa =  readline("Introduce tu peso en Kg : ");
$altura = readline("Introduce tu altura en Mts: ");

if(is_numeric($masa) && is_numeric($altura)){
    $total = floatval($masa) / pow(floatval($altura),2);
    echo "Tu índice de masa corporal es ".round($total,2);
}else{
    echo "Los valores deben ser numéricos";
}