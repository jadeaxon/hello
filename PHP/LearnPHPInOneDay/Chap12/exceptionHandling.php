<?php
//    include "connect.php";
//    echo '<BR>Welcome to Pawszone';

    try{
        include "connect.php";
    }catch(PDOException $e){     
        echo '<BR>Unable to connect '.$e->getMessage();
    }catch(Exception $e){ 
        echo '<BR>Something else happened'.$e->getMessage();
    }finally{ 
        echo '<BR><BR>The finally block is always executed';
    }

    echo '<BR>After connecting';

    function displayUserInput($userInput){
        if ($userInput > 100)
        { 
            throw new OutOfRangeException('<BR>User input is too big');
        }else
        {
            echo '<BR>'.$userInput;
        }
    }


    try
    {
        displayUserInput(105);
//        displayUserInput(16);        
    }catch (OutOfRangeException $e)
    {
        echo $e->getMessage();
    }


    function myExceptionHandler($e)
    {
        echo '<BR>Oppsss... An uncaught exception occurred.<BR>'.$e->getMessage();
    }

    set_exception_handler('myExceptionHandler');

    $pdo = new PDO("some invalid database");
    echo 'This will not be executed';



