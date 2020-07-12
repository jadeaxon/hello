<?php
    date_default_timezone_set('America/New_York');    
    # Strings

    $areacode = "(208)";
    $contact = '+1' . $areacode . '1234567';
    echo $contact;

    echo '<BR>';
    $str1 = 'Good Day!';
    echo strlen($str1);

    $str2 = 'Hello World';
    $str3 = strtolower($str2);
    $str4 = strtoupper($str2);
    echo '<BR>'.$str2;
    echo '<BR>'.$str3;
    echo '<BR>'.$str4;

    echo '<BR>';
    $str5 = ' is ';
    echo 'PHP'.$str5.'Fun<BR>';
    echo 'PHP'.trim($str5).'Fun<BR>';

    $str6 = '**Hello**World***';
    echo trim($str6, '*');

    echo '<BR>';
    $str7 = 'ABCDEF';
    echo substr($str7, 2).'<BR>';
    echo substr($str7, -3).'<BR>';
    echo substr($str7, 2, 1);

    echo '<BR>';
    echo strtotime("next Monday");

    echo '<BR>';
    echo date('d-M-Y', strtotime("+ 10 hours"));

    # Arrays

    $firstArr = array();

    echo '<BR>';
    $secondArr = array(11, 16, 4, 9, 12);    
    echo $secondArr[3]; 
    $secondArr[3] = 20;

    $fruitsArr = array('Apple', 'Banana', 'Coconut');
    
    echo '<BR>';
    $assocArr = array(
        'Peter' => 11,
        'Jane' => 16,
        'Paul' => 12
    );
    echo $assocArr['Paul'];

    echo '<BR>';
    $simpleMDArr = array(	
        array(1, 2, 1, 4, 5),
        array(0, 5, 1, 3, 4),
        array(4, 1, 7, 8, 9)    
    );
    echo $simpleMDArr[2][3];

    echo '<BR>';
    $assocMDArr = array(                
        "first array" => array(1, 2, 6, 1, 3),
        "second array" => array(3, 5, 1, 8, 9),
        "third array" => array(1, 0, 9, 4, 7)
    );
    echo $assocMDArr["first array"][2];

    echo '<BR>';
    $anotherAssocMDArr = array(
        "first player" => array("name" => 'John', "age" => 25),                
        "second player" => array("name" => 'Tim', "age" => 35)
    );
    echo $anotherAssocMDArr["first player"]["age"];

    $myArray = array(2, 5.1, 'PHP', 105);
    echo '<BR>';
    var_dump($myArray); 
    echo '<BR>';    
    print_r($myArray);

    echo '<BR>';
    $addDemo = array(1, 5, 3, 9);        
    $addDemo[] = 7;
    print_r($addDemo);

    echo '<BR>';
    $addDemoAssoc = array('Peter'=>20, 'Jane'=>15);
    $addDemoAssoc['James'] = 17;
    print_r($addDemoAssoc);

    echo '<BR>';
    $colors = array("red", "black", "pink", "white");
    array_splice($colors, 2);
    print_r($colors);

    echo '<BR>';
    $awardwinners = array("Gold"=>"Max", "Silver"=>"Boots", "Bronze"=>"Dora");
    array_splice($awardwinners, 1);
    print_r($awardwinners);

    echo '<BR>';
    $pets = array("corgi", "poodle", "golden retriever", "jack russell");
    array_splice($pets, 1, 2);
    print_r($pets);

    echo '<BR>';
    $countDemo = array(1, 4, 5, 1, 2);
    echo count($countDemo);

    echo '<BR>';
    $indexArrDemo = array(11, 4, 5, 1, 2, 5, 6);
    $assocArrDemo = array('A'=>12, 'B'=>5, 'C'=>20);

    echo array_search(5, $indexArrDemo).'<BR>';
    echo array_search(20, $assocArrDemo).'<BR>';
    var_dump(array_search('B', $assocArrDemo));

    echo '<BR>';
    var_dump(in_array(5, $indexArrDemo));
    var_dump(in_array(20, $assocArrDemo));
    var_dump(in_array('B', $assocArrDemo));

    echo '<BR>';
    $num1 = array(100, 111, 120);
    $num2 = array(100, 3, 5);        
    $num3 = array(1, 10);
    $newArray1 = array_merge($num1, $num2, $num3);
    print_r($newArray1);    

    echo '<BR>';
    $names1 = array(5 => "Peter", 24 => "Aaron");
    $names2 = array(5 => "Zac", 4 => "Alfred", 7 => "Avi");
    $newArray2 = array_merge($names1, $names2);
    print_r($newArray2);

    echo '<BR>';
    $str1 = array('A'=> 12, 'B' => 5, 'C' => 8);
    $str2 = array('A' => 15, 'D' => 10);
    $newArray3 = array_merge($str1, $str2);
    print_r($newArray3);

