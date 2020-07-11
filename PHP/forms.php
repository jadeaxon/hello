<!-- php can run as a local web server for a directory. -->
<!-- Best to run it in another terminal session (like with screen). -->
<!-- php -S localhost:8000 -t . -->
<!-- -S means run php as a web server. -->
<!-- localhost is the machine you are on.  8000 is the port for the server to listen on. -->
<!-- If another service is already using this port, change it to something else. -->
<!-- -t gives the document root.  We use . to set it to the current directory. -->

<!-- Open this URL up in your web browser. -->
<!-- http://localhost:8000/forms.php -->

<!-- A mockup form to create a new user. -->
<html>
	<title>Hello, PHP forms!</title>
    <body>
		<?php
			echo "Hello, PHP forms!\n";
		?>
        <form action="forms.php" method="POST">
            <label>First Name</label>
            <input type="text" name="firstname" id="firstname"/><br>
            <label>Last Name</label>
            <input type="text" name="lastname" id="lastname"/><br>
            <label>Email</label>
            <input type="text" name="email" id="email"/><br>
            <button type="submit">Save</button>
		</form>

		<!-- Show what was posted via this form. -->
		<?php
		if ($_POST) {
			echo "First Name: " . $_POST['firstname'] . "<br>";
			echo "Last Name: " . $_POST['lastname'] . "<br>";
			echo "Email: " . $_POST['email'] . "<br>";
		}
		?>
    </body>
</html>


