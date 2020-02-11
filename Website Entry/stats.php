<?php

if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
	header("location: login.php");
	exit;
}

require_once "config.php";
//require_once "setIntialStatus.php";


$prep1 = $con->query("SELECT id FROM upIps order by id desc limit 1;");
$prep1->execute();
$id = $prep1->fetch(PDO::FETCH_BOTH);
$id = intval(array_pop($id));

$prep2 = $con->prepare('SELECT logFile FROM upIps WHERE id = ?;');
$prep3 = $con->prepare('SELECT ipAddr FROM upIps WHERE id = ?;');
$prep4 = $con->prepare('SELECT PS FROM upIps WHERE id = ?;');


$x = 1;
while($x < $id+1){
	$prep2->bindParam(1,$x,PDO::PARAM_INT);
	$prep2->execute();
	$log = $prep2->fetch(PDO::FETCH_ASSOC);
	$prep3->bindParam(1,$x,PDO::PARAM_INT);
	$prep3->execute();
	$ip = $prep3->fetch(PDO::FETCH_ASSOC);
	$prep4->bindParam(1,$x,PDO::PARAM_INT);
	$prep4->execute();
	$ps = $prep4->fetch(PDO::FETCH_ASSOC);

	$log=array_pop($log);
	$ip=array_pop($ip);
	$ps=array_pop($ps);

	echo"<tr>";
	echo"<th>".$ip."</th>";
	echo"<th>".$ps."</th>";
	echo"<th>".$log."</th>";
	echo"<th>COMMMING SOON!</th>";
	echo"</tr>";

	$x++;

}


?>
