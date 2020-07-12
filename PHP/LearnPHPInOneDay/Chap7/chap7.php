<?php

    function displayGreetings(){
        echo 'Hello';
    }

    displayGreetings();

    echo '<BR>';

    function displayGreetings2($name, $message){
        echo "Hello $name, $message";
    }

    displayGreetings2('Jamie', 'good morning');

    echo '<BR>';

    function displayGreetings3($name, $message = 'have a good day'){
        echo "Hello $name, $message";
    }
    
    displayGreetings3('Jamie');
    echo '<BR>';
    displayGreetings3('Jamie', 'how are you?');

    echo '<BR>';
    
    function addNumbers($num1, $num2, $num3){
        return $num1 + $num2 + $num3;
        echo 'Hello';    
    }

    echo addNumbers(9, 6, 1);

    echo '<BR>';

    echo addNumbers('9', '6', '1');

    echo '<BR>';
