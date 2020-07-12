<!DOCTYPE html>
<html>
	<head><title>PHP Form Handling</title>
	</head>
	<body>
		<form action = "page1-submit-form.php" method = "post">
			Enter Name<BR> <input type = "text" name = "studentname" value = "Your Name"> <BR><BR>
			Favorite Subject(s)<BR> <input type = "checkbox" name = "subj[]" value = "EL">English <input type = "checkbox" name = "subj[]" value = "MA">Math <input type = "checkbox" name = "subj[]" value = "PG">Programming <BR><BR>
			Gender <BR> <input type = "radio" name = "gender" value = "M">Male <input type = "radio" name = "gender" value = "F">Female <BR><BR> <input type = "submit" name="action" value = "Submit Form">
		</form>

	<?php
		session_start();
		if ($_GET) { echo '$_GET: '; print_r($_GET); }
		if ($_POST) { echo '$_POST: '; print_r($_POST); }
	?>

	</body>
</html>
