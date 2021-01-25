<?php
$page = file_get_contents('9_unit_1_ex.html');

$page = str_replace('{page_title}', 'Welcome', $page);
$page = str_replace('{color}', 'green', $page);
$page = str_replace('{name}', 'Galina', $page);

file_put_contents('page.html', $page);