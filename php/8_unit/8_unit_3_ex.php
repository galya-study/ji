<?php

try {
    $db = new PDO('mysql:host=127.0.0.1:3306;dbname=testdb', 'root', 'root');
} catch (PDOException $error) {
    print 'Не удалось подключиться к базе данных: ' . $error->getMessage();
}

function formEnter() 
{
    $q = $GLOBALS['db']->query('SELECT dish_id, dish_name FROM dishes');

    $result = 'Нет блюд для выбора';
    if ($q != null) {
        $result = '<form method="POST" action="8_unit_3_ex.php" enctype="multipart/form-data">
                    <select name="dish" id="dish">';

        while ($row = $q->fetch()) {
            $result .= "<option value=\"$row[dish_id]\">$row[dish_name]</option>";
        }
        $result .= '</select>
            <input type="submit" name="select" id="select" value="Выбрать">
            </form>';
    }

    return $result;
}

function formWithSelectDish() 
{
    $q = $GLOBALS['db']->prepare('SELECT * FROM dishes WHERE dish_id = ?');
    $q->execute([$_POST['dish']]);

    $resultQuery = $q->fetch();

    $spicyFlag = 'No';

    if ($resultQuery['is_spicy'] == 1) {
        $spicyFlag = 'Yes';
    }

    $result = "<table>
                    <tr>
                        <td>ID -</td>
                        <td>{$resultQuery['dish_id']}</td>
                    </tr>
                    <tr>
                        <td>Dish's name -</td>
                        <td>{$resultQuery['dish_name']}</td>
                    </tr>
                    <tr>
                        <td>Is it spicy? -</td>
                        <td>$spicyFlag</td>
                    </tr>
                    <tr>
                        <td>Price -</td>
                        <td>{$resultQuery['price']}</td>
                    </tr>
                </table>";


    return $result;
}

if (isset($_POST['dish'])) {
    print formWithSelectDish();
} else {
    print formEnter();
}