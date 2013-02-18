<?php

for($i=0;$i<2880;$i++) {
$file = file_get_contents("http://finance.yahoo.com/q/op?s=LNKD&m=2012-08");

$f = fopen("LNKD".strval(time())."_12_8.txt","w");
fwrite($f, $file);
fclose($f);
sleep(10);

$file = file_get_contents("http://finance.yahoo.com/q/op?s=LNKD&m=2012-09");

$f = fopen("LNKD".strval(time())."_12_9.txt","w");
fwrite($f, $file);
fclose($f);
sleep(10);

$file = file_get_contents("http://finance.yahoo.com/q/op?s=LNKD&m=2012-11");

$f = fopen("LNKD".strval(time())."_12_11.txt","w");
fwrite($f, $file);
fclose($f);
sleep(10);
}

?>