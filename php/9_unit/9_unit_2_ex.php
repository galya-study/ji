<?php
$addressCount = [];

foreach (file('address.txt') as $row) {
    $row = trim($row);
    if (isset($addressCount[$row])) {
        $addressCount[$row]++;
    } else {
        $addressCount[$row] = 1;
    }
}

arsort($addressCount);

$result = implode(PHP_EOL, array_map(function ($count, $address) {
    return $count . "\t" . $address;
}, $addressCount, array_keys($addressCount)));

file_put_contents('address_count.txt', $result);
