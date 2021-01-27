<?php

try {
    $db = new PDO('mysql:host=127.0.0.1:3306;dbname=testdb', 'root', 'root');
} catch (PDOException $error) {
    print 'Не удалось подключиться к базе данных: ' . $error->getMessage();
}

function showForm() 
{
    $result = '<form method="POST" action="8_unit_4_ex.php" enctype="multipart/form-data">
                <label for="nameClient">Имя: </label>
                <input type="text" name="nameClient" id="nameClient">
                <br>

                <label for="phoneClient">Телефон: </label>
                <input type="text" name="phoneClient" id="phoneClient">
                <br>

                <label for="likeDish">Любимое блюдо: </label>';

    $q = $GLOBALS['db']->query('SELECT dish_id, dish_name FROM dishes');

    if ($q != null) {
        $result .= '<select name="likeDish" id="likeDish">';

        $rows = $q->fetchAll();

        foreach ($rows as $row) {
            $result .= "<option value=\"$row[dish_id]\">$row[dish_name]</option>";
        }
    } else {
        $result .= "<label>Блюда не найдены/</label>";
    }

    $result .= '</select>
                <br>
                <input type="submit" name="add" id="add" value="Добавить">
                </form>';

    return $result;
}

function saveClient()
{
    try {
        $GLOBALS['db']->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $q = $GLOBALS['db']->exec("INSERT INTO clients (nameClient, phone, dish_id) 
                                    VALUES ('{$_POST['nameClient']}', '{$_POST['phoneClient']}', {$_POST['likeDish']})");

        return 'Операция выполнена успешно!';
    } catch (PDOException $error) {
        print 'Не удалось выполнить операцию: ' . $error->getMessage();
    }
}

function checkInfoForm ()
{
    $errors = [];
    if (strlen(trim($_POST['nameClient'])) == 0) {
        $errors[] = 'Введите имя';
    }

    if (strlen(trim($_POST['phoneClient'])) == 0) {
        $errors[] = 'Введите номер телефона';
    }

    if (!filter_input(INPUT_POST, 'likeDish', FILTER_VALIDATE_INT)) {
        $errors[] = 'Неккоретно выбрано блюдо';
    }

    return $errors;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $errors = implode(';<br>', checkInfoForm());
    if ($errors != '') {
        print $errors;
        print showForm();
    } else {
        print saveClient();
        print showForm();
    }
} else {
    print showForm();
}