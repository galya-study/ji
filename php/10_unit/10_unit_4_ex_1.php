<?php

session_start();

function createFirstForm ()
{
    $firstForm = '<form method="POST" action="10_unit_4_ex_2.php" enctype="multipart/form-data">
        <label for="product1">Товар 1</label>
        <input type="number" name="product1" id="product1" value="'
        . (isset($_COOKIE['product1']) ? $_COOKIE['product1'] : '') . '">'
        . '<br>
        <label for="product2">Товар 2</label>
        <input type="number" name="product2" id="product2" value="'
        . (isset($_COOKIE['product2']) ? $_COOKIE['product2'] : '') . '">'
        . '<br>
        <label for="product3">Товар 3</label>
        <input type="number" name="product3" id="product3" value="' 
        . (isset($_COOKIE['product3']) ? $_COOKIE['product3'] : '') . '">'
        . '<br>
        <label for="product4">Товар 4</label>
        <input type="number" name="product4" id="product4" value="'
        . (isset($_COOKIE['product4']) ? $_COOKIE['product4'] : '') . '">'
        . '<br>
        <label for="product5">Товар 5</label>
        <input type="number" name="product5" id="product5" value="' 
        . (isset($_COOKIE['product5']) ? $_COOKIE['product5'] : '') . '">'
        . '<br>
        <label for="product6">Товар 6</label>
        <input type="number" name="product6" id="product6" value="'
        . (isset($_COOKIE['product6']) ? $_COOKIE['product6'] : '') . '">'
        . '<br>
        <input type="submit" id="save" value="Сохранить">
    </form>';

    return $firstForm;
}

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    setcookie('product1', '');
    setcookie('product2', '');
    setcookie('product3', '');
    setcookie('product4', '');
    setcookie('product5', '');
    setcookie('product6', '');

    print 'Заказ удален.';
    print createFirstForm();
} else {
    print createFirstForm();
}
