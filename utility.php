<?
date_default_timezone_set('Canada/Pacific');
function welcome(){
	if(date("H") < 12){
		return "Good morning";
	}elseif(date("H") > 11 && date("H") < 18){
		return "Good afternoon";
	}elseif(date("H") > 17 && date("H") < 23){
		return "Good evening";
	}
}

?>