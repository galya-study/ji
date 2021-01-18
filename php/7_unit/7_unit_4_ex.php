<?php
function checkForm() 
{
    $errors = [];

    if (
        strlen(trim($_POST['indexSend']) != 6 
        || strlen(trim($_POST['indexRecip']) != 6))
    ) {
        $errors[] = "Длина индекса/ов не соответствует формату";
    } 

    if (
        !filter_input(INPUT_POST, 'indexSend', FILTER_VALIDATE_INT) 
        || !filter_input(INPUT_POST, 'indexRecip', FILTER_VALIDATE_INT)
    ) {
        $errors[] = "Индекс/ы не является/ются целым числом";   
    }


}

