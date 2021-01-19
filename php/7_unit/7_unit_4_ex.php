<?php

$regionsArr = array (
    'KRSK' => 'Красноярский край',
    'KHAK' => 'Республика Хакасия',
    'NSK' => 'Новосибирская область',
    'KEMER' => 'Кемеровская область',
);

function checkForm() 
{
    $errors = [];

    if (
        strlen(trim($_POST['indexSend'])) != 6 
        || strlen(trim($_POST['indexRecip'])) != 6
    ) {
        $errors[] = "Длина индекса/ов не соответствует формату";
    } 

    if (
        !filter_input(INPUT_POST, 'indexSend', FILTER_VALIDATE_INT) 
        || !filter_input(INPUT_POST, 'indexRecip', FILTER_VALIDATE_INT)
    ) {
        $errors[] = "Индекс/ы не является/ются целым числом";   
    }

    if (
        !array_key_exists($_POST['regionSend'], $GLOBALS['regionsArr'])
        || !array_key_exists($_POST['regionRecip'], $GLOBALS['regionsArr'])
    ) {
        $errors[] = "Выбран/ы некорректный/ые регион/ы";
    }

    if (
        strlen(trim($_POST['addressSend'])) == 0
        || strlen(trim($_POST['addressRecip'])) == 0
    ) {
        $errors[] = "Адрес/а являются обязательным/и полями";
    }

    if (!filter_input(INPUT_POST, 'weight', FILTER_VALIDATE_FLOAT)) {
        $errors[] = 'Значение поля "Вес" не является числом';
    }

    if (
        filter_input(INPUT_POST, 'weight', FILTER_VALIDATE_FLOAT) 
        && ((int)$_POST['weight'] > 69 || (int)$_POST['weight'] < 0)
    ) {
        $errors[] = "Вес не соответствует заявленным стандартам (0 кг - 68 кг)";
    }

    if (
        !filter_input(INPUT_POST, 'length', FILTER_VALIDATE_INT)
        || !filter_input(INPUT_POST, 'width', FILTER_VALIDATE_INT)
        || !filter_input(INPUT_POST, 'height', FILTER_VALIDATE_INT)
    ) {
        $errors[] = "Параметр/ы размера посылки (Длина, Ширина, Высота) 
        не является/ются числом/ами";
    }

    if (
        filter_input(INPUT_POST, 'length', FILTER_VALIDATE_INT) 
        && ($_POST['length'] > 91 || $_POST['length'] < 0)
    ) {
        $errors[] = "Длина посылки не соответствует заявленным стандартам (0 см - 91 см)";
    }

    if (
        filter_input(INPUT_POST, 'width', FILTER_VALIDATE_INT) 
        && ($_POST['width'] > 91 || $_POST['width'] < 0)
    ) {
        $errors[] = "Ширина посылки не соответствует заявленным стандартам (0 см - 91 см)";
    }

    if (
        filter_input(INPUT_POST, 'height', FILTER_VALIDATE_INT) 
        && ($_POST['height'] > 91 || $_POST['height'] < 0)
    ) {
        $errors[] = "Высота посылки не соответствует заявленным стандартам (0 см - 91 см)";
    }

    return $errors;
}

function lookForm () 
{
    $addressSend = $_POST['indexSend'] . ", " . $GLOBALS['regionsArr'][$_POST['regionSend']] . ", " . $_POST['addressSend'];
    $addressRecip = $_POST['indexRecip'] . ", " . $GLOBALS['regionsArr'][$_POST['regionRecip']] . ", " . $_POST['addressRecip'];
    $weight = $_POST['weight'];
    $length = $_POST['length'];
    $width = $_POST['width'];
    $height = $_POST['height'];

    $result =  "<table>
                    <tr>
                        <td colspan=\"2\">Адрес отправителя</td>
                        <td colspan=\"2\">Адрес получателя</td>
                    </tr>
                    <tr>
                        <td colspan=\"2\">$addressSend</td>
                        <td colspan=\"2\">$addressRecip</td>
                    </tr>
                    <tr>
                        <td colspan=\"2\" ></td>
                    </tr>
                    <tr>
                        <td colspan=\"2\" >Информация о посылке</td>
                    </tr>
                    <tr>
                        <td>Вес</td>
                        <td>Длина</td>
                        <td>Ширина</td>
                        <td>Высота</td>
                    </tr>
                    <tr>
                        <td>$weight</td>
                        <td>$length</td>
                        <td>$width</td>
                        <td>$height</td>
                    </tr>
                </table>";

    return $result;
}

$errors = checkForm();
if ($errors) {
    print(implode(';<br>', $errors));
} else {
    print(lookForm());
}