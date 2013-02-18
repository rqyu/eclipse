<?include 'header.php';?>

<?php
 
$host = '199.195.141.236';
$usr = 'Eclipse';
$pwd = 'hedgefund';
$db = 'Eclipse';
 
$con = mysql_connect('199.195.141.236', 'Eclipse', 'hedgefund');
 
if (!$con) die('Cannot connect: '.mysql_error());
 
mysql_select_db($db, $con);
mysql_query('INSERT INTO Stock_info() VALUES()');

?>

<?include 'footer.php';?>