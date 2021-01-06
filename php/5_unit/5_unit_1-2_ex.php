<?php
function getImg ($url, $alt = null, $height = null, $width = null)
{
    $htmlText = "<img src=\"{$GLOBALS['imagesRoot']}{$url}\"";

    if ($alt !== null) {
        $htmlText .= " alt=\"{$alt}\"";
    }

    if ($height !== null) {
        $htmlText .= " height=\"{$height}\"";
    }

    if ($width !== null) {
        $htmlText .= " width=\"{$width}\"";
    }

    $htmlText .= '>';

    return $htmlText;
}