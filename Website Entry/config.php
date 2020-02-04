<?php

$file = fopen("/home/sam/pull/test.txt","r") or die("Unable to open file!");
$pwd = fread($file, filesize("/home/sam/pull/test.txt"));
$PASSWORD = base64_decode($pwd);

$HOSTNAME = "localhost";
//$PORT = 3306;
$USERNAME = "localUser1";
$DATABASE = "main";
try {
    $con = new PDO("mysql:host=$HOSTNAME;port=3306;dbname=$DATABASE", $USERNAME, $PASSWORD);
    $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
//       echo "connected successfully to mySQL\n";
    }
catch (PDOException $e)
    {
    echo "connection failed: ". $e->getMessage() . "\n";
    }

?>
?>