<?php
$cities = array(
    'Нью-Йорк, шт. Нью-Йорк' => ['NY' => 8175133],
    'Лос-Анджелес, шт. Калифорния' => ['CA' => 3792621],
    'Чикаго, шт. Иллинойс' => ['IX' => 2695598],
    'Хьюстон, шт. Техас' => ['TX' => 2100263],
    'Филадельфия, шт. Пенсильвания' => ['PA' => 1526006],
    'Феникс, шт. Аризона' => ['AZ' => 1445632],
    'Сан-Антонио, шт. Техас' => ['TX' => 1327407],
    'Сан-Диего, шт. Калифорния' => ['CA' => 1307402],
    'Даллас, шт. Техас' => ['TX' => 1197816],
    'Сан-Хосе, шт. Калифорния' => ['CA' => 945942]);

$states = array(
    'NY' => 'шт. Нью-Йорк',
    'CA' => 'шт. Калифорния',
    'IX' => 'шт. Иллинойс',
    'TX' => 'шт. Техас',
    'PA' => 'шт. Пенсильвания',
    'AZ' => 'шт. Аризона');


$state_populations = array();

$all = 0;

print("<table>\n");
print("<tr><td><b>Город</b></td><td><b>Население</b></td></tr>\n");
foreach ($cities as $city => $arr)
{
    foreach ($arr as $state => $population)
    {
        print("<tr><td>$city</td><td>$population</td></tr>\n"); 
        $all = $all + $population; 
        
        if (array_key_exists($state, $states))
        {
            $state_populations[$state] = $state_populations[$state] + $population;
        }
        else
        {
            $state_populations[$state] = $population;
            
        }
    }   
}
print("<tr><td>Сумма</td><td>$all</td></tr>\n"); 
print("</table>");

print("<table>\n");
print("<tr><td><b>Штат</b></td><td><b>Население</b></td></tr>\n");
foreach ($state_populations as $state => $population)
{
    print("<tr><td>$states[$state]</td><td>$population</td></tr>\n"); 
}
print("</table>");
?>