<?php
$file = fopen('dishes.csv','rb');

if (!feof($file)) {
    print '<table>';
    while ((!feof($file)) && ($line = fgetcsv($file))) {
        print "<tr><td>{$line[0]}</td>
                <td>{$line[1]}</td>
                <td>{$line[2]}</td></tr>";
    }
    print '</table>';
}

fclose($file);