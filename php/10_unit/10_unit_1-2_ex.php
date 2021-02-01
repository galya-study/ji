<?php

$countVisit = 0;

if (isset($_COOKIE['countVisit'])) {
    $countVisit = $_COOKIE['countVisit'] + 1;
}

setcookie('nameUser', 'galya');

if ($_COOKIE['countVisit'] == 20) {
    setcookie('countVisit', 1);
} else {
    setcookie('countVisit', $countVisit);
}

if ($_COOKIE['countVisit'] % 5 == 0 and $_COOKIE['countVisit'] != 0) {
    print("Number of views: {$_COOKIE['countVisit']}");
}

