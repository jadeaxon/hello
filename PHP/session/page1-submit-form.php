<?php
	# Capture data posted by previous page action to session.
	# This will make it accessible on the next page we route to.
	session_start();
	$_SESSION['name'] = $_POST['studentname'];

	header("Location: page2.php");
?>
