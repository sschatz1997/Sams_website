<?php
date_default_timezone_set("America/New_York");
session_start();

if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
	header("location: login.php");
	exit;
}

require_once "config.php";

/*function getID()
{
	$db1 = new myDB();
	$result = $db1->query('SELECT id FROM companiesBasic order by id desc limit 1;');
	//$result->execute();
	$results = $result->fetchArray();
	$id = intval(array_pop($results));
	return $id+1;
}*/

//$id = getID();

if(isset($_POST["name"])){
	$name = $_POST['name'];
	$web = $_POST['website'];
	$scope = $_POST['scope'];
	$insert = $con->prepare('INSERT INTO companiesBasic(name, website, scope) VALUES (?,?,?)');
//	$insert->bindParam(1,$id, PDO::PARAM_INT);
	$insert->bindParam(1,$name, PDO::PARAM_STR,500);
	$insert->bindParam(2,$web, PDO::PARAM_STR,500);
	$insert->bindParam(3,$scope, PDO::PARAM_STR,500);
	$insert->execute();
}else{
	//echo "an error has occured!<br>";
}
?>

<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Bug Bounty Insert Page</title>
	<hr>
	<center><h1><strong>Bug Bounty Insert Page</center></h1></center>
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
		<center>Bug Bounty Entry</center>
		<center><h1>ONLY ENETER COMPANIES WITH FULL SAFE HARBOR!!!!</h1></center>
		<center><h1>ONLY ENETER COMPANIES WITH MONEY REWARDS!!!!</h1></center>
	</div>	
	<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
		<center><table style="width 100%">
			<tr>
				<th>Enter the company name</th>
				<th>Enter the company website</th>
				<th>Enter the scope, with ; between the different sites</th>
			</tr>
			<tr>		
				<th><input type="text" name="name" id="size1" placeholder="?"><br></th>
				<th><input type="text" name="website" id="size2" placeholder="?"><br></th>
				<th><input type="text" name="scope" id="size3" placeholder="?"><br></th>
			</tr>
		</table></center>
		<center><input type="submit" value="submit"></center> 
	</form>
	</hr>
	<center><p><strong>

	</strong></p></center>
</body>
</html
