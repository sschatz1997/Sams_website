<?php

$file = fopen("/home/sam/pull/test.txt","r") or die("Unable to open file!");
$pwd = fread($file, filesize("/home/sam/pull/test.txt"));
$PASSWORD = base64_decode($pwd);

$HOSTNAME = "localhost";
//$PORT = 3306;
$USERNAME = "localUser1";
$DATABASE = "main";

?>