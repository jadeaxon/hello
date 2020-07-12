<?php

    function myErrorHandler($errno, $errstr, $errfile, $errline)
    {
        echo '<BR>Oppsss... An error occurred.<BR>'.$errstr;
    }

    set_error_handler('myErrorHandler');

    echo $a;
    echo '<BR>Script is not terminated';

    function myShutDownHandler(){

        $lastError = error_get_last();

        if (isset($lastError)) { 
            echo '<BR>Oppsss... Script terminated.<BR>';
        }
    }

    register_shutdown_function('myShutDownHandler');

//    ini_set('display_errors', '0');
    hello();

