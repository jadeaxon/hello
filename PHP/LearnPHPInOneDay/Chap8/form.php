<!DOCTYPE html>
<html>
<head><title>PHP Form Handling</title></head>
<body>        
<form action = "" method = "get">            
<!--<form action = "" method = "post">-->
    Enter Name <BR>
    <input type = "text" name = "studentname" value = "Your Name">
    <BR><BR>
    Favorite Subject(s)<BR>               
    <input type = "checkbox" name = "subj[]" value = "EL">English
    <input type = "checkbox" name = "subj[]" value = "MA">Math
    <input type = "checkbox" name = "subj[]" value = "PG">Programming
    <BR><BR>
    Gender <BR>
    <input type = "radio" name = "gender" value = "M">Male
    <input type = "radio" name = "gender" value = "F">Female
    <BR><BR>    
    <input type = "submit" name="sm" value = "Submit Form">     
</form>    
        
<?php
        
//    if (isset($_GET['sm']))
//        print_r($_GET);
        
//    if (isset($_POST['sm']))
//        print_r($_POST);
        
//    if (isset($_POST['studentname']))
//        echo 'You entered '.$_POST['studentname'].' into the text field';

//    if (isset($_POST['studentname']))
//        echo 'You entered '.htmlspecialchars($_POST['studentname']).' into the text field';
        
?>
        
</body>
</html>


