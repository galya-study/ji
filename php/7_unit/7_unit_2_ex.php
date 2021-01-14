<?php

function process_form () 
{
    //var_dump($_POST);

    $result = '<!DOCTYPE html>
    <html>
    
    <head>
        <meta charset="utf-8">
        <title>test 7 ex 2</title>
    </head>
    
    <body>';

    $result .= "Braised Noodles with {$_POST['noodle']}.";
    $result .= "<br>";

    $result .= 'Sweet: ' . implode(', ', $_POST['sweet']) . '.';
    
    $result .= '<br>';

    $result .= "Sweet Quantity: {$_POST['sweet_q']}.";

    $result .= '</body>';

    return $result;
}

print(process_form());