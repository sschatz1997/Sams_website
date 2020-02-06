<?php
date_default_timezone_set("America/New_York");
session_start();

if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
	header("location: login.php");
	exit;
}

require_once "config.php";

if(isset($_POST["chap"])){
	$chap = $_POST['chap'];
	$term = $_POST['term'];
	$scope = $_POST['def'];
	$insert = $con->prepare('INSERT INTO secPlusDefs(chapter, term, def) VALUES (?,?,?)');
	$insert->bindParam(1,$chap, PDO::PARAM_INT);
	$insert->bindParam(2,$term, PDO::PARAM_STR,100);
	$insert->bindParam(3,$def, PDO::PARAM_STR,500);
	$insert->execute();
}
?>

<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Sec+ Defs Entry</title>
	<hr>
	<!--<center><h1><strong>Bug Bounty Insert Page</center></h1></center>-->
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
		<center>Sec+ Defs Entry</center>
	</div>	
	<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
		<center><table style="width 100%">
			<tr>
				<th>Enter the Chapter Number.</th>
				<th>Enter the Term.</th>
				<th>Enter the Definition.</th>
			</tr>
			<tr>		
				<th><input type="number" name="chap" id="size1" placeholder="?"><br></th>
				<th><input type="text" name="term" id="size2" placeholder="?"><br></th>
				<th><input type="text" name="def" id="size3" placeholder="?"><br></th>
			</tr>
		</table></center>
		<center><input type="submit" value="submit"></center> 
	</form>
	</hr>
	<center><p><strong>

	</strong></p></center>
</body>
</html
