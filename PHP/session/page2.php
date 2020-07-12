<?php
	# Load session data into $_SESSION.
	session_start();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Hello, PHP!</title>
</head>
<body>
	<h1>Hello, <?php echo $_SESSION['name']; ?>!</h1>
    <?php
        # Simple hello world page.
		echo "Hello, PHP (on XAMPP)!\n";
	?>
	<hr/>
	<?php
		if ($_GET) { echo '$_GET: '; print_r($_GET); }
		if ($_POST) { echo '$_POST: '; print_r($_POST); }
		if ($_SESSION) { echo '$_SESSION: '; print_r($_SESSION); }
	?>

</body>
</html>

