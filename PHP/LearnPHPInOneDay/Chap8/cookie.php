<?php    
    setcookie('userName', 'Joy', time() + 120);

    #modifying a cookie
    setcookie('userAge', 25, time() + 3600);
    setcookie('userAge', 26, time() + 3600);

    #deleting a cookie
    setcookie('userLevel', 3, time() + 3600);
    setcookie('userLevel', 3, time() - 3600);
