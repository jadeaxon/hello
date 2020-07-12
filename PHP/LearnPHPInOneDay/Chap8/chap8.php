<?php
    $a = 5;
    $b = NULL;

    var_dump(isset($a));
    var_dump(isset($b));
    var_dump(isset($c));

    echo '<BR>';
    $num = '12.5abc';
    echo filter_var($num, FILTER_SANITIZE_NUMBER_INT);

    echo '<BR>';
    $email = 'abc@gmail';
    var_dump(filter_var($email, FILTER_VALIDATE_EMAIL));
