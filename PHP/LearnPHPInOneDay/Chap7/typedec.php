<?php 

    declare(strict_types=1);


    function addNumbersStrict(int $num1, int $num2, int $num3){
        return $num1 + $num2 + $num3;
    }

//    echo addNumbersStrict('9', '6', '1');

    echo addNumbersStrict(9, 6, 1);


    function addTwoNums($a, $b): int {
        return $a + $b;
    }

    echo '<BR>'.addTwoNums(3, 1);
//    echo '<BR>'.addTwoNums(3.9, 1);