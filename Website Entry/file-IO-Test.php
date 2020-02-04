<?php
$file = fopen("/home/sam/pull/test.txt","r") or die("Unable to open file!");
$pwd = fread($file, filesize("test.txt"));
echo "Non-base64\n";
echo $pwd . "\n";
echo "With the type: " . gettype($pwd) . "\n";
echo "Base64\n";
$b64 = base64_encode($pwd);
echo $b64 . "\n";
$arg = " ";
echo "With the type: " . gettype($arg) . "\n";
echo "With the type: " . gettype($b64) . "\n";

fclose($file);

?>
