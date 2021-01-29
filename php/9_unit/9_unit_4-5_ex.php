<?php

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    print '<form method="POST" action="9_unit_4_ex.php" enctype="multipart/form-data">
                <input type="text" name="file" name="file">
                <br>
                <br>
                <input type="submit" name="send" value="Отправить">
            </form>';
} else {
    $filePath = $_SERVER['DOCUMENT_ROOT'] . '/9_unit/' . $_POST['file'];
    print implode(';<br>', checkFile($filePath));
    print printFile($filePath);
}

function checkFile ($filePath)
{
    $errors = [];
    if (!file_exists($filePath)) {
        $errors[] = 'Файл не найден.';
    } elseif (mb_substr($filePath, -3) == 'php') {
        $errors[] = 'Файлы php недоступны для просмотра';
    } elseif (!is_readable($filePath)) {
        $errors[] = 'Файл недоступен для чтения';
    }

    return $errors;
}

function printFile ($filePath)
{
    return file_get_contents($filePath);
}