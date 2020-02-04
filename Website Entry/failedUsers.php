<?php
require_once "config.php";

$loop = $con->query('SELECT id from logginAttempts order by id desc limit 1;');
$loop->execute();
$entries = $loop->fetch(PDO::FETCH_BOTH);
$entries = intval(array_pop($entries));

/*$loop1 = $con->query('SELECT id from logins1 order by id desc limit 1;');
$loop1->execute();
$entries2 = $loop->fetch(PDO::FETCH_BOTH);
$entries2 = intval($entries);*/

$prep = $con->query('SELECT username FROM logginAttempts;');
$prep->execute();
//$name = $prep->fetch_array(PDO::FETCH_BOTH);

$prep2 = $con->prepare('SELECT time1 FROM logginAttempts WHERE username = ?;');
//$prep3 = $con->prepare('SELECT time1 FROM logins1 WHERE username = ?;');
$prep3 = $con->prepare('SELECT id FROM logginAttempts WHERE username = ? ORDER BY id DESC LIMIT 1;');
$prep4 = $con->prepare('SELECT time1 FROM logginAttempts WHERE id = ?;');
$prep5 = $con->prepare('SELECT ip FROM logginAttempts WHERE id = ?;');

//echo "entries: " . $entries;

$x = 0;
$masterTime = [];
//echo "<th>".$tt."<th>";
while($x < $entries){
	
	$name = $prep->fetch(PDO::FETCH_BOTH);
	$un = array_pop($name);
	$prep2->bindParam(1,$un,PDO::PARAM_STR, 50);
	$prep2->execute();
	$date1 = $prep2->fetch(PDO::FETCH_BOTH);
    if(gettype($date1) != "boolean"){
        $date = array_pop($date1);
    }else{
        $date = "N/A";
    }

	$prep3->bindParam(1,$un,PDO::PARAM_STR, 50);
	$prep3->execute();
	$id = $prep3->fetch(PDO::FETCH_BOTH);
    if(gettype($id) != "boolean"){
        $id = intval(array_pop($id));
        $prep4->bindParam(1,$id,PDO::PARAM_INT);
        $prep4->execute();
        $time1 = $prep4->fetch(PDO::FETCH_BOTH);
        $time1 = array_pop($time1);
        
        $prep5->bindParam(1,$id,PDO::PARAM_INT);
        $prep5->execute();
        $ip = $prep5->fetch(PDO::FETCH_BOTH);
        $ip = array_pop($ip);
    }else{
        $id = 0;
        $time1 = "N/A";
        $ip = "N/A"
    }

	
	echo"<tr>";
	echo "<th>".$un."</th>";
	echo "<th>".$date."</th>";
    echo "<th>".$time1."</th>";
    echo "<th>".$ip."</th>";
	echo"</tr>";
	$x++;
} 

$test1 = "test1";


?>
