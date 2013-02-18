<?
$q = $_GET["q"];
$fname = 'script.R';
$f = fopen($fname, 'w') or die("cannot open");
fwrite($f, $q);
fclose($f);
$scr = 'R --no-save < script.R > a.out';
echo $scr.'         ';
$output = shell_exec($scr);
$f = fopen('a.out', 'r');
echo $a;
$a = fread($f, filesize($f));
echo $a;
fclose($f);
?>