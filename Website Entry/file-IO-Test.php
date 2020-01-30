<?php
$file = fopen("test.txt","r") or die("Unable to open file!");
echo fread($file, filesize("test.txt"));
fclose($file);

?>