<html>

<head>
<meta http-equiv="Content-Type" content="text/html;charset=gb2312" />
<meta name="keywords" content="俞瑞启,ruiqiyu,Azurewrath" />

<title>Eclipse Service</title>
</head>

<body>

<?php

function get_options($ticker, $option) {

if ($option == "Yahoo") {
	$page = file_get_contents("http://finance.yahoo.com/q/op?s=".$ticker."+Options");
} else if ($option == "Google") {
	$page = file_get_contents("http://www.google.com/finance/option_chain?q=NASDAQ:".$ticker);
}

$file_name = $ticker.strval(time())."_option.txt";

$f = fopen($file_name, 'w');

fwrite($f, $page);

fclose($f);

return $file_name;

}

?>

<form name="option" id="option" action="stock.php" method="POST">
<input type="radio" name="finance_" value="Google" checked="checked"/>Google
<input type="radio" name="finance_" value="Yahoo" />Yahoo<br />
<input type="text" name="ticker_" />
<input type="submit" name="get_ticker_" value="Get option data for ticker (eg. enter GOOG)" />
</form>
<?php
$ticker = $_POST["ticker_"];
$finance = $_POST["finance_"];
$name = get_options($ticker, $finance);

if(strlen($ticker)!=4) {
	echo "Invalid ticker";
} else {
	exec("python process_option.py ".$name);
	$file = "temp.txt";
	if(!file_exists($file)) die("Invalid ticker");
	$result = file_get_contents("temp.txt");
	echo $result;
	unlink($file);
}

?>
</body>

</html>