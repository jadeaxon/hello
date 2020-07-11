<!-- php can run as a local web server for a directory. -->
<!-- Best to run it in another terminal session (like with screen). -->
<!-- php -S localhost:8000 -t . -->
<!-- -S means run php as a web server. -->
<!-- localhost is the machine you are on.  8000 is the port for the server to listen on. -->
<!-- If another service is already using this port, change it to something else. -->
<!-- -t gives the document root.  We use . to set it to the current directory. -->

<!-- Open this URL up in your web browser. -->
<!-- http://localhost:8000/create_user_form.php -->

<!-- Use PHP to get posted form fields, connect to database, and insert new user record. -->
<?php
    if ($_POST) {
		// Validation.
		if (!$_POST['firstname'] || !$_POST['lastname'] || !$_POST['email']){
            exit("All fields are required.");
        }

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
			// Connect to the MySQL database via PDO.
            $conn = new PDO("mysql:host=$host;dbname=$database", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

			// A parameterized SQL statement.  Parameters begin with :.
            $sql = "INSERT INTO users (firstname, lastname, email) VALUES (:firstname, :lastname, :email)";
			$statement = $conn->prepare($sql);

			// Pass form fields (from HTTP POST) as args to compiled SQL statement.
            $statement->execute([
                "firstname" => $_POST["firstname"],
                "lastname" => $_POST["lastname"],
                "email" => $_POST["email"]
            ]);

        }
        catch(PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
    }
?>
<html>
    <body>
        <form action="create_user_form.php" method="POST">
            <label>First Name</label>
            <input type="text" name="firstname" id="firstname"/>
            <br>
            <label>Last Name</label>
            <input type="text" name="lastname" id="lastname"/>
            <br>
            <label>Email</label>
            <input type="text" name="email" id="email"/>
            <br>
            <button type="submit">Save</button>
        </form>
    </body>
</html>
