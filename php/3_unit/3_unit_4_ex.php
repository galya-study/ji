<?php
//нужно вывести температуру по Фаренгейту и Цельсию, 
//известна температура по Фаренгейту, формула для Цельсия:
//C = (F - 32) * 5 / 9
for ($f_t = -50; $f_t < 51; $f_t++)
{
    $c_t = ($f_t - 32) * 5 / 9;

    printf("F: %6.2f, C: %6.2f\n", $f_t, $c_t);
}
?>