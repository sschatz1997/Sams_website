<?php
session_start();

if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
	header("location: login.php");
	exit;
}

require_once "config.php";
//require_once "setIntialStatus.php";

function getIP()
{
	if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
	    $ip = $_SERVER['HTTP_CLIENT_IP'];
	} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
	    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
	} else {
	    $ip = $_SERVER['REMOTE_ADDR'];
	}
	return $ip;
}

?>
<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>sams page</title>
	<hr>
	<center><h1><strong>sams site</center></h1></center>
	<link="stylesheet" href="landingPage1.css">
	<link="stylesheet" href="dropdown.css">
	<link="stylesheet" href="main.css">
	<hr>
</head>

<body>
	<?php setcookie("gotyounow",$_SESSION["username"]);?>
	<hr>
	<div class="navbar">
	<a href="/index.php">Home</a>
	<a href="index.php">Profile</a>
	<?php if(htmlspecialchars($_SESSION["username"]) == "admin"){echo"<a href='index.php'>Dashboard</a>";}?>
	<div class="1">
		<form action="logout.php" method="POST">
			<center><input type="submit" value="logout" name="logout"></span></center>
		</form>
	</div>

	<div class="page-header">
		<center>welcome</center>
	</div>
	<center><p><strong>
		WORK IN PROGRESS
			WORK IN PROGRESS
				WORK IN PROGRESS
					WORK IN PROGRESS
						WORK IN PROGRESS
					WORK IN PROGRESS
				WORK IN PROGRESS
			WORK IN PROGRESS
		WORK IN PROGRESS
	</strong></p></center>
</body>
</html