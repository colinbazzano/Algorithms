#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # obtain the values from recipe & ingredients
    batches = []
    for key, value in recipe.items():
        print(key, value)
        if not ingredients.get(f"{key}"):
            return 0
        batches.append(ingredients[key] // value)
        print(ingredients[key])

    return min(batches)
    # loop through recipes
    # loop through ingredients
    # compare if recipe values is smaller than ingredients values (of all)
    # indicate one batch can be made, subtract the ingredients available and continue


recipe = {'milk': 100, 'butter': 50, 'flour': 5}
ingredients = {'milk': 132, 'butter': 48, 'flour': 51}

# recipe_batches(recipe, ingredients)

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
