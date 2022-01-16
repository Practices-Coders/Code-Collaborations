<?php
$ahorros = readline("Introduce la cantidad de ahorros en dolares: ($) ");
$locale = 'es_ES';
$nf = new NumberFormatter($locale,NumberFormatter::ORDINAL);
if(is_numeric($ahorros)){
    for($i=1;$i<=3;$i++){
        $total = $ahorros + ($ahorros * 0.3) * $i;
        $total = floatval($total);
        echo "El total de ahorros tras el ".$nf->format($i)." año ".round($total,2)."\n";
    }
    
}