<?php

class Database {
	# TO DO: Read these from a configuration class instance.
	private $host = "127.0.0.1";
	private $username = "jadeaxon";
	private $password = "flCsoXBFnugSTFs58A93";
	private $database = "php";

	private $connection; # Database handle/connection.

	public function connect() {
		// PHP Data Objects (PDO).  Works with MySQL, Oracle, and others.
		$this->connection = new PDO(
			"mysql:host=$this->host;dbname=$this->database",
			$this->username,
			$this->password
		);
		$this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

	}

	public function listUsers() {
		$conn = $this->connection;

		$users = $conn->query('SELECT * FROM users')->fetchAll(PDO::FETCH_ASSOC);
		print_r($users);
	}

}

?>

