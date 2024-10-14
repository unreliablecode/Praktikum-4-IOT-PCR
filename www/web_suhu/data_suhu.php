<?php


    //Variabel database
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "database_baru";


    $conn = mysqli_connect("$servername", "$username", "$password","$dbname");


    // Prepare the SQL statement
    
    $result = mysqli_query ($conn,"INSERT INTO datasensor (data) VALUES ('".$_GET["data"]."')");    
    
    if (!$result) 
        {
            die ('Invalid query: '.mysqli_error($conn));
        }  
?>
