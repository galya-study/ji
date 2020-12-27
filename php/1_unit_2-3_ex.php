<?php 

//присваивание стоимости меню
$hamburger = 4.95;
$milkshake = 1.95;
$cola = 0.85;

//определение процента дополнительных выплат
$tax = 0.075;
$tips = 0.16;


$meal = 2 * $hamburger + $milkshake + $cola; //стоимость всей еды
$total_tax = $meal * $tax; //налог
$total_tips = $meal * $tips; //чаевые 
$total_cost = $total_tax + $total_tips + $meal; //стоимость общая

//определение первой строки таблицы
printf("%s%8s%5s", '|', 'Meal', '|'); // выравнивание вправо с пробелами
printf("%7s%2s", 'Amount', '|');
printf("%6s%3s\n", 'Cost', '|');

printf("%'-32s\n", '');

//еда
printf("%s%10s%3s", '|', 'Hamburger', '|');
printf("%2s%7s", '2', '|');
printf("%6s%3s\n", '4.95', '|');

printf("%s%10s%3s", '|', 'Milkshake', '|');
printf("%2s%7s", '1', '|');
printf("%6s%3s\n", '1.95', '|');

printf("%s%5s%8s", '|', 'Cola', '|');
printf("%2s%7s", '1', '|');
printf("%6s%3s\n", '0.85', '|');

printf("%'-32s\n", '');

//налог и чаевые
printf("%s%20s%2s", '|', 'Tax', '|');
printf("%6.2f%3s\n", $total_tax, '|');
printf("%s%20s%2s", '|', 'Tips', '|');
printf("%6.2f%3s\n", $total_tips, '|');

printf("%'-32s\n", '');

//общая стоимость
printf("%s%20s%2s", '|', 'Total cost', '|');
printf("%6.2f%3s\n", $total_cost, '|');

printf("%'-32s\n", '');

?>