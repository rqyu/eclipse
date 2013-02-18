<html>
<title>Eclipse</title>

<head>
	<link href="./style/eclipse_style.css" rel="stylesheet" type="text/css">
	<script type="text/javascript">
	function submitR(f) {
		var xmlhttp;
		var x=f.inputbox.value;
		if (window.XMLHttpRequest) {
			xmlhttp=new XMLHttpRequest();
		} else {
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		
		xmlhttp.onreadystatechange=function() {
			if(xmlhttp.readyState==4 && xmlhttp.status==200) {
				document.getElementById("result").innerHTML=xmlhttp.responseText;
			}
		}
		
		xmlhttp.open("GET","calculate.php?q="+x,true);
		xmlhttp.send();
	}
	</script>
</head>

<body>
<form name="rcode" method="GET">
Enter your code in the box:<br>
<textarea cols="60" rows="10" name="inputbox" value=""></textarea>
<input type="button" name="submit" value="submit" onClick="submitR(this.form)">
</form>
<div id="result"></div>
</body>

</html>