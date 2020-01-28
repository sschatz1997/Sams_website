<?php
ini_set('display_errors', 'On');
error_reporting(E_ALL);
date_webault_timezone_set("America/New_York");

class myDB extends SQLite3
{
		function __construct()
		{
			$this->open('BB.db');
		}
}

function sqliteTestConect()
{
	$db1 = new myDB();
	if(!$db1){
		echo $db->lastErrorMsg();
	}else{
		echo "opened SQLITE3\n";
	}
}

function getID()
{
	$db1 = new myDB();
	$result = $db1->query('SELECT id FROM companiesBasic order by id desc limit 1;');
	//$result->execute();
	$results = $result->fetchArray();
	$id = intval(array_pop($results));
	return $id+1;
}

$db1 = new myDB();
$id = getID();
$name = $_POST['name'];
$scope = $_POST['scope'];
$web = $_POST['website'];

$insert = $db1->prepare('INSERT INTO companiesBasic(id, name, website, scope) VALUES (?,?,?,?);');
$insert->bindValue(1,$id, SQLITE3_INTEGER);
$insert->bindValue(2,$name, SQLITE3_TEXT);
$insert->bindValue(3,$term, SQLITE3_TEXT);
$insert->bindValue(4,$web, SQLITE3_TEXT);
$insert->execute();
//$insert->commit();
header("location: bb.html")
//sqliteTestConect();
//echo "lastErrorMsg: ". $res->lastErrorMsg();
//}

?>