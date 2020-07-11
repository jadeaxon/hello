<?php
$host = "127.0.0.1";
$username = "jadeaxon";
$password = "flCsoXBFnugSTFs58A93";
$database = "php";

try {
	$conn = new PDO("mysql:host=$host;dbname=$database", $username, $password);
	$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

	$sql = "DELETE FROM users WHERE id = :id";
	$statement = $conn->prepare($sql);
	$statement->execute(['id' => 1]);
	echo $statement->rowCount() . " row(s) deleted.";

}
catch(PDOException $e) {
	echo "Connection failed: " . $e->getMessage();
}
?>

