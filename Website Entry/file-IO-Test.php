<?php
$file = fopen("test.txt","r") or die("Unable to open file!");
$pwd = fread($file, filesize("/home/sam/pull/test.txt"));
echo "Non-base64\n";
echo $pwd . "\n";
echo "Base64\n";
$b64 = base64_encode($pwd);
echo $b64 . "\n";

fclose($file);

?>
