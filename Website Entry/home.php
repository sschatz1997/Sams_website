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
/*created by Samuel Schatz                #
# github: https://github.com/sschatz1997  #
# email: sjschatz@captechu.edu            */
?>
<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>sams page</title>
	<hr>
	<style>
		tr, th, table{
			border: 4px solid black;
			border-collapse: collapse;
			width: 100%;
			white-space: nowrap;
		}
	</style>
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
			<button class="dropbtn">IP Log Tables
				<i class="fa fa-caret-down"></i>
            </button>
			<div class="dropdown-content">
				<a href="ufwLogTable.php">UFW Table</a>
				<a href="sysLogTable.php">Syslog Table</a>
				<a href="apacheLogTable.php">Apache Table</a>
				<a href="apacheErrorLogTable.php">Apache Error Table</a>
				<a href="mysqlLogTable.php">MySql Table</a>
                <a href="ftpLogTable.php">FTP Table</a>
            </div>
		</div>
		<div class="dropdown">
			<button class="dropbtn">Study forms
				<i class="fa fa-caret-down"></i>
			</button>
			<div class="dropdown-content">
				<a href="bb.php">Bug Bountiy Entry</a>
				<a href="secPlus.php">Sec+ Defs Entry</a>
			</div>
		</div>
		<?php if(htmlspecialchars($_SESSION["username"]) == "admin"){echo"<a href='dashboard.php'>Dashboard</a>";}?>
		<div class="1">
			<form action="logout.php" method="POST">
				<center><input type="submit" value="logout" name="logout"></span></center>
			</form>
		</div>
    </div>
	<div class="page-header">
		<center>welcome</center>
	</div>
	</hr>
	<center><h1>IP's that are up and can be nmaped!<h1></center>

	<table>
		<tr>
			<th> IP </th>
			<th> PS </th>
			<th> log </th>
			<th> add to nmap queue</th>
		</tr>
		<?php require_once("stats.php");?>
	</table>
	<!--<center><p><strong>
		WORK IN PROGRESS
			WORK IN PROGRESS
				WORK IN PROGRESS
					WORK IN PROGRESS
						WORK IN PROGRESS
					WORK IN PROGRESS
				WORK IN PROGRESS
			WORK IN PROGRESS
		WORK IN PROGRESS
	</strong></p></center>-->
</body>
</html
