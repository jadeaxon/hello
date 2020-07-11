<!-- Create the php.users table on the local MySQL instance. -->

<?php
	// PRE: MySQL is installed on localhost.
	// PRE: php database has been created.
	// PRE: PHP Data Objects (PDO) driver has been installed.
	// Use Cygwin installer to install php-pdo_mysql package.
	// PRE: PDO driver does not support default authentication plugin used by MySQL 8+.
	// Thus, you need to do this:
	// ALTER USER jadeaxon IDENTIFIED WITH mysql_native_password BY '<password for jadeaxon>';

	// Database connection args.
	// $host = "localhost"; // FAIL: Uses a Unix socket instead of a TCP/IP socket.
	$host = "127.0.0.1";
    $username = "jadeaxon";
    $password = "flCsoXBFnugSTFs58A93";
    $database = "php";

    try {
        $conn = new PDO("mysql:host=$host;dbname=$database", $username, $password);

        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

		$sql = "
			CREATE TABLE users(
				id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
				firstname VARCHAR(30) NOT NULL,
				lastname VARCHAR(30) NOT NULL,
				email VARCHAR(30) NOT NULL
			);
		";

		$statement = $conn->prepare($sql);
        $statement->execute();

	}
    catch (PDOException $e) {
		echo "Connection failed: " . $e->getMessage();
    }
?>


