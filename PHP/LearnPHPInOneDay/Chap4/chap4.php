<?php

    define("BASIC_MEMBER", 1112020);
    echo BASIC_MEMBER;
    echo '<BR>';
    define("BASIC_MEMBER", 16932);
    echo BASIC_MEMBER;

    echo '<BR>';

    echo 'BASIC_MEMBER';

    echo '<BR>';    
    $x = 7;
    echo $x;

    echo '<BR>';
    $x = 5;
    echo $x;

    echo '<BR>';
    echo '$x';

    echo '<BR>';
    echo 'The value is $x.';
    echo '<BR>';
    echo "The value is $x.";

    $x = 5;
    $y = 2.1;
    $z = true;
    echo '<BR>';
    var_dump($x);
    var_dump($y);
    var_dump($z);

    echo '<BR>';
    $p = (int)4.6;
    var_dump($p);

    echo '<BR>';
    $x = 5;
    $y = 2;
    echo $x + $y; echo '<BR>';
    echo $x - $y; echo '<BR>';
    echo $x*$y; echo '<BR>';
    echo $x/$y; echo '<BR>';
    echo $x%$y; echo '<BR>';
    echo $x**$y; echo '<BR>';

    $x = 5;
    $x += 3;
    echo $x;

    $q = 3;
    echo "<BR>$q<BR>";
    echo ++$q;
//    echo $q++;
//    echo "<BR>$q<BR>";

