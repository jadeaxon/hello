<?php

// Section A - Connecting to the database

$pdo = new PDO("mysql:host=127.0.0.1;port=3307;dbname=pawszone", "pz_admin", "ABCD");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Section B - SELECT all rows from pets

$sql = "SELECT petname, owner FROM pets";
$stmt = $pdo->prepare($sql);

$stmt->execute();

while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    echo '<BR>Owner = '.$row['owner'].'<BR>';
    echo 'Pet Name = '.$row['petname'].'<BR>';
}

$stmt->execute();

while ($row = $stmt->fetch(PDO::FETCH_NUM)) {
    echo '<BR>Owner = '.$row[1].'<BR>';
    echo 'Pet Name = '.$row[0].'<BR>';
}


