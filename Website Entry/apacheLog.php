<?php
require_once "config.php";
$log = "/var/log/apache2/access.log";
$prep1 = $con->prepare('SELECT logFile from fromLogs WHERE logFile = "?" order by id desc limit 1;');
$prep1->bindParam(1,$log,PDO::PARAM_STR,100);
$prep1->execute();
$entries = $prep1->fetch(PDO::FETCH_BOTH);
$entries = count($entries);

//$name = $prep->fetch_array(PDO::FETCH_BOTH);

$prep2 = $con->prepare('SELECT created_at FROM users WHERE username = ?;');
//$prep3 = $con->prepare('SELECT time1 FROM logins1 WHERE username = ?;');
$prep3 = $con->prepare('SELECT id FROM logins1 WHERE username = ? ORDER BY id DESC LIMIT 1;');
$prep4 = $con->prepare('SELECT time1 FROM logins1 WHERE id = ?;');
$prep5 = $con->prepare('SELECT ip FROM logins1 WHERE id = ?;');

//echo "entries: " . $entries;
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
while($x < $entries){
	
	$name = $prep->fetch(PDO::FETCH_BOTH);
	$un = array_pop($name);
	$prep2->bindParam(1,$un,PDO::PARAM_STR, 50);
	$prep2->execute();
	$date1 = $prep2->fetch(PDO::FETCH_BOTH);
	$date = array_pop($date1);
	
	$prep3->bindParam(1,$un,PDO::PARAM_STR, 50);
	$prep3->execute();
	$id = $prep3->fetch(PDO::FETCH_BOTH);
	$id = intval(array_pop($id));

	$prep4->bindParam(1,$id,PDO::PARAM_INT);
	$prep4->execute();
	$time1 = $prep4->fetch(PDO::FETCH_BOTH);
    $time1 = array_pop($time1);
    
    $prep5->bindParam(1,$id,PDO::PARAM_INT);
    $prep5->execute();
    $ip = $prep5->fetch(PDO::FETCH_BOTH);
    $ip = array_pop($ip);
	
	echo"<tr>";
    echo "<th>".$time1."</th>";
    echo "<th>".$ip."</th>";
	echo"</tr>";
	$x++;
} 

$test1 = "test1";


?>
