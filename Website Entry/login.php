<?php
// Initialize the session
session_start();
 
// Check if the user is already logged in, if yes then redirect him to welcome page
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: home.php");
    exit;
}
 
// Include config file
require_once "config.php";
//require_once "setIntialStatus.php";
 
// Define variables and initialize with empty values
$username = $password = "";
$username_err = $password_err = "";

class myDB extends SQLite3
{
		function __construct()
		{
            $this->open('temp.db');
            //needs to change
		}
}

function sqliteTestConect()
{
	$db1 = new myDB();
	if(!$db1){
		echo $db->lastErrorMsg();
	}else{
		//echo "opened SQLITE3\n";
	}
}

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


function failed($time, $usr, $pwd)
{
	$db1 = new myDB();
	$ip = getIP();
	$prep = $db1->prepare("INSERT INTO failedLogins(username, pasword, time, ip) VALUES (?,?,?,?);");
	$prep -> bindValue(1,$usr);
	$prep -> bindValue(2,$pwd);
	$prep -> bindValue(3,$time);
	$prep -> bindValue(4,$ip);
	$prep -> execute();	
	header("location: login.php");
	
}

function failed2($usr)
{
    $ip = getIP();
	$prep1 = $con->prepare("SELECT atempts FROM logginAttempts WHERE username = ?");
	$prep1 -> bindParam(1,$usr,PDO::PARAM_STR,50);
	$prep1 -> execute();
	$attempts = $prep1->fetch(PDO::FETCH_BOTH);
	if($attempts == false){
		$attempts = 1;
		//below checks if the user exists
		$prep0 = $con->prepare("SELECT username FROM logginAttempts WHERE username = ?");
		$prep0 -> bindParam(1,$usr,PDO::PARAM_STR,50);
		$prep0 -> execute();
		$userExist = $prep0->fetch(PDO::FETCH_BOTH);
		if($userExist == false){
			$insrt = True;
		}else{
			$insrt = False;
		}
	} else {
		$attempts = intval(array_pop($attempts));
	}
	if($insrt == True){
		//update
		$bans = 0;
		$prep2 = $con->prepare("INSERT INTO logginAttempts(username, atempts, numOfBans, ip) VALUES (?,?,?,?);");
		$prep2->bindParam(1,$usr,PDO::PARAM_STR,50);
		$prep2->bindParam(2,$attempts,PDO::PARAM_INT);
        $prep2->bindParam(3,$bans,PDO::PARAM_INT);
        $prep2->bindParam(4,$ip,PDO::PARAM_STR,30);
		$prep2->execute();
	}else{
		//insert
		$prep3 = $con->prepare("SELECT numOfBans FROM logginAttempts WHERE username = ?");
		$prep3 -> bindParam(1,$usr,PDO::PARAM_STR,50);
		$prep3 -> execute();
		$bans = $prep3->fetch(PDO::FETCH_BOTH);
		$bans = intval(array_pop($prep3));
		if($attempts == 3){ //|| $attempts + 1 = 3){
			$attempts = 0;
			$bans = $bans + 1;
			$prep4 = $con->prepare("INSERT INTO logginAttempts(username, atempts, numOfBans, ip) VALUES (?,?,?,?);");
			$prep4->bindParam(1,$usr,PDO::PARAM_STR,50);
			$prep4->bindParam(2,$attempts,PDO::PARAM_INT);
			$prep4->bindParam(3,$bans,PDO::PARAM_INT);
            $prep4->bindParam(4,$ip,PDO::PARAM_STR,30);
			$prep4->execute();
		}else{
			$attempts = $attempts + 1;
			$prep4 = $con->prepare("INSERT INTO logginAttempts(username, atempts, numOfBans, ip) VALUES (?,?,?,?);");
			$prep4->bindParam(1,$usr,PDO::PARAM_STR,50);
			$prep4->bindParam(2,$attempts,PDO::PARAM_INT);
            $prep4->bindParam(3,$bans,PDO::PARAM_INT);
            $prep4->bindParam(4,$ip,PDO::PARAM_STR,30);
			$prep4->execute();
		}
	}
	
}

/* if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
} */
$ip = $_SERVER['REMOTE_ADDR'];
// Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){

    // Check if username is empty
    if(empty(trim($_POST["username"]))){
        $username_err = "Please enter username.";
    } else{
        $username = trim($_POST["username"]);
    }
    
    // Check if password is empty
    if(empty(trim($_POST["password"]))){
        $password_err = "Please enter your password.";
    } else{
        $password = trim($_POST["password"]);
    }
    
    // Validate credentials
    if(empty($username_err) && empty($password_err)){
        // Prepare a select statement
        $sql = "SELECT id, username, password FROM users WHERE username = :username";
	$s2 = $con->prepare('INSERT INTO logins1(username, ip) VALUES (?,?);');
        
        if($stmt = $con->prepare($sql)){
            // Bind variables to the prepared statement as parameters
            $stmt->bindParam(":username", $param_username, PDO::PARAM_STR);
	    $s2->bindParam(1, $username, PDO::PARAM_STR, 50);
            $s2->bindParam(2, $ip, PDO::PARAM_STR, 30);
            // Set parameters
            $param_username = trim($_POST["username"]);
            
            // Attempt to execute the prepared statement
            if($stmt->execute()){
                // Check if username exists, if yes then verify password
                if($stmt->rowCount() == 1){
                    if($row = $stmt->fetch()){
                        $id = $row["id"];
                        $username = $row["username"];
                        $hashed_password = $row["password"];
                        if(password_verify($password, $hashed_password)){
                            // Password is correct, so start a new session
                            session_start();
                            
                            // Store data in session variables
                            $_SESSION["loggedin"] = true;
                            $_SESSION["id"] = $id;
                            $_SESSION["username"] = $username;
                            // Redirect user to welcome page
			    //require_once "loginT.php";
			    $s2->execute();
                            header("location: home.php");
                        } else{
                            // Display an error message if password is not valid

                            $password_err = "The password you entered was not valid.";
                        }
                    }
                } else{
                    // Display an error message if username doesn't exist
                    $username_err = "Login Failed";
		    $time = time();
		    failed($time, $username, $password);
                }
            } else{
                echo "Oops! Something went wrong. Please try again later.";
            }
        }
        
        // Close statement
        unset($stmt);
    }
    
    // Close connection
    unset($con);
}
?>
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
    <style type="text/css">
        body{ font: 14px sans-serif; }
        .wrapper{ width: 350px; padding: 20px; }
    </style>
</head>
<body>
    <div class="wrapper">
        <h2>Login</h2>
        <p>Please fill in your credentials to login.</p>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div class="form-group <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
                <label>Username</label>
                <input type="text" name="username" class="form-control" value="<?php echo $username; ?>">
                <span class="help-block"><?php echo $username_err; ?></span>
            </div>    
            <div class="form-group <?php echo (!empty($password_err)) ? 'has-error' : ''; ?>">
                <label>Password</label>
                <input type="password" name="password" class="form-control">
                <span class="help-block"><?php echo $password_err; ?></span>
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Login">
            </div>
            <p>Don't have an account? <a href="reg.php">Sign up now</a>.</p>
        </form>
    </div>
</body>
</html>
