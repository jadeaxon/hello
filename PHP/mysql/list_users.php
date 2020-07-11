<?php
$host = "127.0.0.1";
$username = "jadeaxon";
$password = "flCsoXBFnugSTFs58A93";
$database = "php";

try {
	$conn = new PDO("mysql:host=$host;dbname=$database", $username, $password);
	$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

	$statement = $conn->prepare("SELECT * FROM users WHERE email = :email");
	$statement->execute(['email' => 'nobody@nowhere.tld']);
	$statement->setFetchMode(PDO::FETCH_ASSOC);

	// This fetches only the first matching user.
	$user = $statement->fetch();

	echo "<pre>";
	print_r($user);
	echo "</pre>";

	$users = $conn->query('SELECT * FROM users')->fetchAll(PDO::FETCH_ASSOC);
	echo "<h2>All Users</h2>";
	echo "<pre>";
	print_r($users);
	echo "</pre>";

}
catch(PDOException $e) {
	echo "Connection failed: " . $e->getMessage();
}
?>

