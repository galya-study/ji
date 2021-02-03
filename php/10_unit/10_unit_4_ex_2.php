<?php

function createFirstForm ()
{
    $firstForm = '<form method="POST" action="10_unit_4_ex_1.php" enctype="multipart/form-data">
            <label>Товар 1 - </label>
            <label>Количество '
            . $_POST['product1'] . '</label>
            <br>
            <label>Товар 2 - </label>
            <label>Количество '
            . $_POST['product2'] . '</label>
            <br>
            <label>Товар 3 - </label>
            <label>Количество '
            . $_POST['product3'] . '</label>
            <br>
            <label>Товар 4 - </label>
            <label>Количество '
            . $_POST['product4'] . '</label>
            <br>
            <label>Товар 5 - </label>
            <label>Количество '
            . $_POST['product5'] . '</label>
            <br>
            <label>Товар 6 - </label>
            <label>Количество '
            . $_POST['product6'] . '</label>
            <br>
            <input type="hidden" id="chekOut" name="chekOut" value="chekOut">
            <input type="submit" id="checkOut" value="Оформить заказ">
        </form>
        <form method="POST" action="10_unit_4_ex_1.php" enctype="multipart/form-data">
            <input type="submit" id="prevPage" value="Отредактировать заказ">
        </form>';

    return $firstForm;
}

session_start();

$_SESSION['product1'] = $_POST['product1'];
$_SESSION['product2'] = $_POST['product2'];
$_SESSION['product3'] = $_POST['product3'];
$_SESSION['product4'] = $_POST['product4'];
$_SESSION['product5'] = $_POST['product5'];
$_SESSION['product6'] = $_POST['product6'];

print createFirstForm();