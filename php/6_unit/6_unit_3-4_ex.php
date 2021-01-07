<?php

class Entree
{
    public $name;
    public $ingredients = array();
    public function __construct($name, $ingredients)
    {
        $this->name = $name;
        $this->ingredients = $ingredients;
    }

    public function hasIngredient($ingredient)
    {
        return in_array($ingredient, $this->ingredients);
    }
}

class PriceEntree extends Entree
{
    public function __construct($name, $ingredients)
    {
        parent::__construct($name, $ingredients);

        foreach ($this->ingredients as $ingredient) {
            if (!($ingredient instanceof \Food\Ingredient)) {
                throw new Exception('$ingredient должен быть типа Ingredient');
            }
        }
    }

    public function getTotalCost()
    {
        $totalCost = 0;

        foreach ($this->ingredients as $ingredient){
            $tempCost = $ingredient->getCost();
            $totalCost += $tempCost;
        }

        return $totalCost;
    }
}