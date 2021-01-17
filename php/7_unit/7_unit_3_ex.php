<?php
function checkForm ()
{
    $errors = [];
    if (strlen($_POST['operand1']) == 0 || $_POST['operand2'] == 0) {
        $errors[] = "Не введено значение/я операнда/ов";
    }

    if ($_POST['operand1'] != 0 && $_POST['operand2'] != 0) {
        $ok1 = filter_input(INPUT_POST, 'operand1', FILTER_VALIDATE_FLOAT);
        if (is_null($ok1) || ($ok1 == false)) {
            $errors[] = "Операнд 1 не является числом";
        }

        $ok2 = filter_input(INPUT_POST, 'operand1', FILTER_VALIDATE_FLOAT);
        if (is_null($ok2) || ($ok2 == false)) {
            $errors[] = "Операнд 2 не является числом";
        }
    }

    return implode($errors);
}

function calculate () 
{
    $operand1 = $_POST['operand1'];
    $operand2 = $_POST['operand2'];
    $operation = $_POST['operation'];
    $result = null;

    if ($operation == "+") {
        $result = $operand1 + $operand2;
    } elseif ($operation == "-") {
        $result = $operand1 - $operand2;
    } elseif ($operation == "*") {
        $result = $operand1 * $operand2;
    } else {
        $result = $operand1 / $operand2;
    }

    return "{$_POST['operand1']}{$_POST['operation']}{$_POST['operand2']} = $result";
}

if (checkForm() != "") {
    print(checkForm());
} else {
    print(calculate());
}
