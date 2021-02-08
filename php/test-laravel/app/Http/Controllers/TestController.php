<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class TestController extends Controller
{
    public function test()
    {
        return view('welcome', [
            'array' => [1, 2, 3],
        ]);
    }
}
