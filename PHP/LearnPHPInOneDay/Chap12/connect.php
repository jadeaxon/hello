<?php

    $pdo = new PDO("mysql:host=localhost;dbname=pawszone", "wrongadmin", "ABCD");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
