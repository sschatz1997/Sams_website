<?php
require_once "config.php";
$log = "/var/log/ufw.log";
$prep0 = $con->query('SELECT id FROM fromLogs WHERE logFile = "/var/log/ufw.log";');
$prep0->execute();
$count2 = $prep0->rowCount();
$prep1 = $con->prepare('SELECT id from fromLogs WHERE logFile = ?;');
$prep1->bindParam(1,$log,PDO::PARAM_STR,100);
$prep1->execute();
$entries = $prep1->fetch(PDO::FETCH_BOTH);
//$entries = $prep1->fetchAll(PDO::FETCH_ASSOC);
if(is_array($entries)){
	//$count = count($entries);
//	echo "Their are : ". $count . "<br>";
//	print_r($entries);
}else{
	echo "error";
}

$prep2 = $con->prepare('SELECT ipAddr from fromLogs WHERE id = ?;');
$prep3 = $con->prepare('SELECT timeSubmitted from fromLogs WHERE id = ?;');

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
$id = intval(array_pop($entries));
while($x < $count2){
	$prep2->bindParam(1,$id,PDO::PARAM_INT);
	$prep2->execute();
	$ip = $prep2->fetch(PDO::FETCH_ASSOC);
	//echo "type: " . gettype($ip) . "<br>";
	$prep3->bindParam(1,$id,PDO::PARAM_INT);
	$prep3->execute();
	$ip = array_pop($ip);
	$date = $prep3->fetch(PDO::FETCH_ASSOC);
	$date = array_pop($date);

	
	echo"<tr>";
    echo "<th>".$log."</th>";//logfile
	echo "<th>".$ip."</th>";//ipaddr
	echo "<th>".$date."</th>";//date submitted
	echo"</tr>";
	$id++;
	$x++;
} 

$test1 = "test1";

/*created by Samuel Schatz                #
# github: https://github.com/sschatz1997  #
# email: sjschatz@captechu.edu            */
?>
