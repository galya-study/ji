<?php
function decToHex (int $red, int $green, int $blue)
{
    $hexArr[] = dechex($red);
    $hexArr[] = dechex($green);
    $hexArr[] = dechex($blue);

    foreach ($hexArr as $i => $value) {
        if (strlen($value) == 1) {
            $hexArr[$i] = '0' . $value;
        }
    };

    $hex = '#' . implode('', $hexArr);

    return $hex;
}

print(decToHex(220, 20, 60));