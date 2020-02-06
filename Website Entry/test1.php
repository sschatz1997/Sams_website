<?php
require_once "config.php";
$log = "/var/log/apache2/access.log";
$prep1 = $con->prepare('SELECT logFile from fromLogs WHERE logFile = "?" order by id desc limit 1;');
$prep1->bindParam(1,$log,PDO::PARAM_STR,100);
$prep1->execute();
$entries = $prep1->fetch(PDO::FETCH_BOTH);
$count = count($entries);

echo "Their are : ". $count;
?>