<?php

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    print '<form method="POST" action="9_unit_4_ex.php" enctype="multipart/form-data">
                <input type="text" name="file" name="file">
                <br>
                <br>
                <input type="submit" name="send" value="Отправить">
            </form>';
}

function checkFile ()
{
    
}