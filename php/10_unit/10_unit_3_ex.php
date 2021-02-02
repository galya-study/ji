<?php
session_start();

$form = '<form method="POST" action="10_unit_3_ex.php" enctype="multipart/form-data">
        <label for="colour">Выберите цвета фона:</label>
        <br>
        <select name="colour" id="colour">
            <option value="red">Красный</option>
            <option value="green">Зеленый</option>
            <option value="blue">Синий</option>
        </select>
        <br>
        <input type="submit" name="choose" value="Выбрать">
        </form>';

$coloursArr = [
    "red" => "Красный",
    "green" => "Зеленый",
    "blue" => "Синий",
];

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    $printFirstPage = "<body" 
        . (isset($_SESSION['colourBG']) ? " bgcolor=\"{$_SESSION['colourBG']}\"" : '') 
        . '>' . $form . '</body>';

    print $printFirstPage;
} else {
    $colour = $_POST['colour'];
    $printSecondPage = "<body bgcolor=\"$colour\">
    <label>Вы выбрали {$coloursArr[$colour]}</label>
    </body>";

    $_SESSION['colourBG'] = $colour;

    print $printSecondPage;
}