<?php

$file = fopen("test.txt","r") or die("Unable to open file!");
$pwd = fread($file, filesize("test.txt"));

$HOSTNAME = "localhost";
//$PORT = 3306;
$USERNAME = "localUser1";
$DATABASE = "main";

?>