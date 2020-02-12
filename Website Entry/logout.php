<?php
$choice = $_POST['logout'];

if($choice == "logout"){
	// Initialize the session
	session_start();
	 
	// Unset all of the session variables
	$_SESSION = array();
	 
	// Destroy the session.
	session_destroy();
	 
	// Redirect to login page
	header("location: login.php");
	exit;
}

/*created by Samuel Schatz                #
# github: https://github.com/sschatz1997  #
# email: sjschatz@captechu.edu            */
?>