<?php

    var_dump(5 == 5);
    var_dump('Hello' == 'Hello');
    var_dump(5 == 5.0);

    echo '<BR>';
    var_dump(5 === 5);
    var_dump(5 === 5.0);

    echo '<BR>';
    var_dump(5 != 7);
    var_dump(5 <> 7);

    echo '<BR>';
    var_dump(5 !== 5.0);

    echo '<BR>';
    var_dump(7 > 2);

    echo '<BR>';
    var_dump(8 >= 5);
    var_dump(6 >= 6);

    echo '<BR>';
    var_dump(9 < 12);

    echo '<BR>';
    var_dump(10 <= 14);
    var_dump(13 <= 13);

    echo '<BR>';
    var_dump(5 <=> 7);
    var_dump(5 <=> 5.0);

    echo '<BR>';
    var_dump(!(5 > 10));

    echo '<BR>';
    $a = 5 > 3 and 4 < 10;
    $b = 5 > 3 && 4 < 10;
    $c = 5 > 1 && 13 < 5;

    var_dump($a);
    var_dump($b);
    var_dump($c);

    echo '<BR>';
    $d = 3 > 2 && 3 < 1;
    $e = 3 > 2 and 3 < 1;
    var_dump($d);
    var_dump($e);

    echo '<BR>';
    $f = 4 < 7 || 10 > 3;
    $g = 3 < 2 || 3 > 1;
    $h = 10 > 15 || 12 < 1;
    var_dump($f);
    var_dump($g);
    var_dump($h);

    echo '<BR>';
    $a = 7;
//    $a = -2;
//    $a = 3;
//    $a = 11;
    if ($a < 0)
    {
        echo 'if block<BR>';
        echo '$a is smaller than 0';
    }
    elseif ($a < 5)
        echo 'First elseif block';
    elseif ($a < 10)
        echo 'Second elseif block';
    else
        echo 'Else block';

    echo '<BR>';
    $a = (7 == 7 ? 'Yes' : 'No');
    //$a = (7 > 10 ? 'Yes' : 'No');
    echo $a;

    echo '<BR>';
    $b = 20;
    switch ($b)
    {
        case 10:
            echo 'Chocolate<BR>';
            break;
        case 20:
            echo 'Lemon<BR>';
        case 25:
            echo 'Strawberry<BR>';
            break;
        default:
            echo 'None of the above<BR>';
    }

    for ($c = 1; $c < 5; ++$c){
        echo 'The value of $c is '.$c.'<BR>';
    }

    $arr1 = array(11, 12, 13, 14, 15);

    foreach ($arr1 as $num){
        echo 'The number is '.$num.'<BR>';
    }

    $arr2 = array('Aaron'=>12, 'Ben'=>23, 'Carol'=>35);

    foreach ($arr2 as $name=>$age){
        echo $name.' is '.$age.' years old.<BR>';
    }

    $d = 1;

    while ($d < 5)
    {
        echo 'The value of $d is '.$d.'<BR>';
        $d++;
    }

    $e = 100;

    do {
        echo 'The value is '.$e;
        $e++;
    } while ($e<0);

    echo '<BR>';
    if ("hello")
        echo 'if block';
    else
        echo 'else block';

    echo '<BR>';
    for ($i = 0; $i < 50; ++$i)        
    {
        echo "$i<BR>";    
        if ($i == 4)
            break;    
    }

    for ($i = 0; $i < 6; ++$i)        
    {
        echo '$i = '.$i.', ';

        if ($i == 4)
            continue;  

        echo 'First.';
        echo 'Second.<BR>';
    }

    $a = 5;

    if ($a == 5){
        echo '<BR>The value of $a is<BR>';
        echo $a;
    }else{
        echo 'Not five';
    }


    $a = 5;

    if ($a == 5):
        echo '<BR>The value of $a is<BR>';
        echo $a;
    else:
        echo 'Not five';
    endif;
?>

<?php
    for ($i = 0; $i < 3; ++$i):
        echo '<h1>Hello</h1>';
    endfor;
?>

<?php
    for ($i = 0; $i < 3; ++$i): ?>
        <h1>Hello</h1>
    <?php endfor;
?>
