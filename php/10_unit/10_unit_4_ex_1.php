<?php

function createFirstForm ()
{
    $firstForm = '<form method="POST" action="10_unit_4_ex_2.php" enctype="multipart/form-data">
        <label for="product1">Товар 1</label>
        <input type="number" name="product1" id="product1" value="'
        . (isset($_SESSION['product1']) ? $_SESSION['product1'] : '') . '">'
        . '<br>
        <label for="product2">Товар 2</label>
        <input type="number" name="product2" id="product2" value="'
        . (isset($_SESSION['product2']) ? $_SESSION['product2'] : '') . '">'
        . '<br>
        <label for="product3">Товар 3</label>
        <input type="number" name="product3" id="product3" value="' 
        . (isset($_SESSION['product3']) ? $_SESSION['product3'] : '') . '">'
        . '<br>
        <label for="product4">Товар 4</label>
        <input type="number" name="product4" id="product4" value="'
        . (isset($_SESSION['product4']) ? $_SESSION['product4'] : '') . '">'
        . '<br>
        <label for="product5">Товар 5</label>
        <input type="number" name="product5" id="product5" value="' 
        . (isset($_SESSION['product5']) ? $_SESSION['product5'] : '') . '">'
        . '<br>
        <label for="product6">Товар 6</label>
        <input type="number" name="product6" id="product6" value="'
        . (isset($_SESSION['product6']) ? $_SESSION['product6'] : '') . '">'
        . '<br>
        <input type="submit" id="save" value="Сохранить">
    </form>';

    return $firstForm;
}

session_start();

if (isset($_POST['chekOut'])) {

    unset($_SESSION['product1']);
    unset($_SESSION['product2']);
    unset($_SESSION['product3']);
    unset($_SESSION['product4']);
    unset($_SESSION['product5']);
    unset($_SESSION['product6']);

    print createFirstForm();
} else {
    print createFirstForm();
}