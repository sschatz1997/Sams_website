<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);
require_once "config.php";

//function failed3(usrname)
$usr = "sam";
$prep1 = $con->prepare("SELECT atempts FROM logginAttempts WHERE username = ?");
$prep1 -> bindParam(1,$usr,PDO::PARAM_STR,50);
$prep1 -> execute();
$attempts = $prep1->fetch(PDO::FETCH_BOTH);

if(is_bool($attempts)){
	echo "this works<br>";
} else {
	echo "it doesnt<br>";
}

/*echo "The type is: " . gettype($attempts) . "\n";
echo "attempts " . $attempts;    */


?>
