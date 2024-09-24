# test_data_structures.py

from data_structures import (
    get_names,
    get_spiciest_foods,
    print_spicy_foods,
    get_spicy_food_by_cuisine,
    print_spiciest_foods,
    get_average_heat_level,
    create_spicy_food
)

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

def test_get_names():
    assert get_names(spicy_foods) == ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def test_get_spiciest_foods():
    assert get_spiciest_foods(spicy_foods) == [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]

def test_get_spicy_food_by_cuisine():
    assert get_spicy_food_by_cuisine(spicy_foods, "American") == {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
    assert get_spicy_food_by_cuisine(spicy_foods, "Thai") == {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}

def test_get_average_heat_level():
    assert get_average_heat_level(spicy_foods) == 6

def test_create_spicy_food():
    new_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
    updated_list = create_spicy_food(spicy_foods, new_food)
    assert new_food in updated_list
