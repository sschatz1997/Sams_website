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
	<link rel="stylesheet" href="landingPage1.css">
	<link rel="stylesheet" href="dropdown.css">
	<link rel="stylesheet" href="main.css">
	<hr>
</head>

<body>
	<?php setcookie("gotyounow",$_SESSION["username"]);?>
	<hr>
	<div class="navbar">
		<a href="home.php">Home</a>
		<a href="home.php">Profile</a>
		<div class="dropdown">
			<button class="dropbtn">Study forms
				<i class="fa fa-caret-down"></i>
			</button>
			<div class="dropdown-content">
				<a href="bb.php">Bug Bountiy Entry</a>
			</div>
		</div>
		<?php if(htmlspecialchars($_SESSION["username"]) == "admin"){echo"<a href='home.php'>Dashboard</a>";}?>
		<div class="1">
			<form action="logout.php" method="POST">
				<center><input type="submit" value="logout" name="logout"></span></center>
			</form>
		</div>
    </div>
    <div class="wrapper">
		<div id="left"><!--change to left later-->
			<table>
                <tr>
					<th>Users</th>
					<th>Date Created</th>
                    <th>Last Log-in</th>
                    <th>IP address</th>
                </tr>
	        	<?php require_once "curentUsers.php";?>
            </table>
        </div>
		<!--<div id="right">change to left later
			<table>
                <tr>
					<th>Username</th>
					<th>Date last attempted</th>
                    <th>IP address</th>
                </tr>
	        	<?php require_once "failedUsers.php";?>
            </table>
        </div>-->



    </div>
    
</body>
</html>
