<?php

try {
    $db = new PDO('mysql:host=127.0.0.1:3306;dbname=testdb', 'root', 'root');
} catch (PDOException $err) {
    print("Не удалось подключиться к базе данных: " . $err->getMessage());
}

$q = $db->query('SELECT * FROM dishes ORDER BY price');
while ($row = $q->fetch()) {
    print "$row[dish_name] <br>";
}