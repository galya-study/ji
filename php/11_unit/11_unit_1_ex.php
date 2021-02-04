<?php
$releases = file_get_contents("https://php.net/releases/?json");
if ($releases === false) {
    print 'Не удалось получить';
    
} else {
    var_dump($releases);
}