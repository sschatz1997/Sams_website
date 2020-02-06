<?php
require_once "config.php";
$log = "/var/log/apache2/access.log";
$prep1 = $con->prepare('SELECT id from fromLogs WHERE logFile = ?;');
$prep1->bindParam(1,$log,PDO::PARAM_STR,100);
$prep1->execute();
$entries = $prep1->fetch(PDO::FETCH_BOTH);
//$entries = $prep1->fetchAll(PDO::FETCH_ASSOC);
if(is_array($entries)){
	$count = count($entries);
//	echo "Their are : ". $count . "<br>";
//	print_r($entries);
	$prep2 = $con->prepare('SELECT ipAddr from fromLogs WHERE id = ?;');
	$prep3 = $con->prepare('SELECT timeSubmitted from fromLogs WHERE id = ?;')
}else{
	echo "error";
}


/*
fromLogs
+---------------+--------------+------+-----+-------------------+-------------------+
| Field         | Type         | Null | Key | Default           | Extra             |
+---------------+--------------+------+-----+-------------------+-------------------+
| id            | int          | NO   | PRI | NULL              | auto_increment    |
| logFile       | varchar(100) | NO   |     | NULL              |                   |
| ipAddr        | varchar(30)  | NO   |     | NULL              |                   |
| timeSubmitted | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| dateSubmitted | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+---------------+--------------+------+-----+-------------------+-------------------+
*/
$x = 0;
$masterTime = [];
//echo "<th>".$tt."<th>";
while($x < $count){
	$id = intval(array_pop($entries));
	$prep2->bindParam(1,$id,PDO::PARAM_INT);
	$prep3->bindParam(1,$id,PDO::PARAM_INT);
	$ip = $prep2->fetch(PDO::FETCH_BOTH);
	$ip = array_pop($ip);
	$date = $prep2->fetch(PDO::FETCH_BOTH);
	$date = array_pop($date);

	
	echo"<tr>";
    echo "<th>".$log."</th>";//logfile
	echo "<th>".$ip."</th>";//ipaddr
	echo "<th>".$date."</th>";//date submitted
	echo"</tr>";
	$x++;
} 

$test1 = "test1";


?>
