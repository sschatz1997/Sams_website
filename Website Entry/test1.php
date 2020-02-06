<?php
require_once "config.php";
$log = "/var/log/apache2/access.log";
$prep1 = $con->prepare('SELECT ipAddr from fromLogs WHERE logFile = ?;');
$prep1->bindParam(1,$log,PDO::PARAM_STR,100);
$prep1->execute();
$entries = $prep1->fetch(PDO::FETCH_BOTH);
//$entries = $prep1->fetchAll(PDO::FETCH_ASSOC);
if(is_array($entries)){
	$count = count($entries);
	echo "Their are : ". $count . "<br>";
	print_r($entries);
}else{
	echo "is not an array " . gettype($entries) . "<br>";
}
?>
