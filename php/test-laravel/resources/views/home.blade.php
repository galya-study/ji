@extends('layouts.app')

@section('title')
    Главная страница
@endsection

@section('content')
    <h1>Главная страница</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia nam nostrum corporis qui ipsum eveniet distinctio porro rerum temporibus a ducimus deserunt praesentium facere, numquam quas optio voluptatem et! Labore?</p>
@endsection

@section('aside')
    @parent
    <p>Дополнительный текст</p>
@endsection