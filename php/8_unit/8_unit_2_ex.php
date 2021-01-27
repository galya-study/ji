<?php

try {
    $db = new PDO('mysql:host=127.0.0.1:3306;dbname=testdb', 'root', 'root');
} catch (PDOException $err) {
    print "Не удалось подключиться к базе данных: " . $err->getMessage();
}


if (filter_input(INPUT_POST, 'approximatePrice', FILTER_VALIDATE_FLOAT)) {
    $approximatePrice = $_POST['approximatePrice'];
    $q = $db->prepare('SELECT dish_name, price FROM dishes WHERE price <= ?');
    $q->execute([$approximatePrice]);
    
    print "<table>";
    print "<tr><td>Dish</td><td>Price</td></tr>";

    while ($row = $q->fetch()) {
        print "<tr><td>$row[dish_name]</td><td>$row[price]</td></tr>";
    }
    print "</table>";   
} else {
    print 'Введеное значение не является числом';
}