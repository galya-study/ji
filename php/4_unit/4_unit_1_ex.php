<?php
$city_arr = array(
    'Нью-Йорк' => 8175133,
    'Лос-Анджелес, шт. Калифорния' => 3792621,
    'Чикаго, шт. Иллинойс' => 2695598,
    'Хьюстон, шт. Техас' => 2100263,
    'Филадельфия, шт. Пенсильвания' => 1526006,
    'Феникс, шт. Аризона' => 1445632,
    'Сан-Антонио, шт. Техас' => 1327407,
    'Сан-Диего, шт. Калифорния' => 1307402,
    'Даллас, шт. Техас' => 1197816,
    'Сан-Хосе, шт. Калифорния' => 945942);

$all = 0;

print("<table>\n");
print("<tr><td><b>City</b></td><td><b>Population</b></td></tr>\n");
foreach ($city_arr as $key => $value)
{
    print("<tr><td>$key</td><td>$value</td></tr>\n"); 
    $all = $all + $value;   
}
print("<tr><td>Сумма</td><td>$all</td></tr>\n"); 
print("</table>");
?>