<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);
require_once "config.php";

function getIP()
{
	if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
	    $ip = $_SERVER['HTTP_CLIENT_IP'];
	} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
	    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
	} else {
	    $ip = $_SERVER['REMOTE_ADDR'];
	}
	return $ip;
} 

$ip = getIP();

//function failed3(usrname)
$usr = "sam";
$prep1 = $con->prepare("SELECT atempts FROM logginAttempts WHERE username = ?");
$prep1 -> bindParam(1,$usr,PDO::PARAM_STR,50);
$prep1 -> execute();
$attempts = $prep1->fetch(PDO::FETCH_BOTH);

echo "The type for ip address is " . gettype($ip) . "\n";

if(is_bool($attempts)){
	echo "this works<br>";
} else {
	echo "it doesnt<br>";
}

/*echo "The type is: " . gettype($attempts) . "\n";
echo "attempts " . $attempts;    */


?>
