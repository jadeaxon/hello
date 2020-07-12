<?php
    include 'AwardWinningMovie.php';
    $awm = new AwardWinningMovie('A12324', 'Max', 6.99, 'Best Picture');
    
    echo $awm->recommend('Japan');

//    echo $awm->displayHeading('H1');


//    $mv = new Movie('A3244', 'Golden Rose', 3.99);
//    echo $mv->displayHeading('H1'); 
