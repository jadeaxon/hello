<?php

include "Database.php";

$database = new Database();
$database->connect();
$database->listUsers();

?>
