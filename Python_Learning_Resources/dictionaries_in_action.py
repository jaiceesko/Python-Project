#!/usr/bin/env python3

## Dictionaries in action

# basic dictionary oprations

recipes = {'oil':'olive oil', 'ham':2, 'eggs':3, 'bread':2, 'onion':1}

print(recipes)

print(recipes['oil'])

print(len(recipes))

print('bread' in recipes)

list_recipes = list(recipes.keys())

print(list_recipes)

for recipe in list_recipes:
    print(recipe.title())

if 'ketchup' in  recipes:
    print('')
else:
    recipes['ketchup'] = 1

print(recipes)


# changing dictionaries in place

recipes['eggs'] = ['bake', 'boil', 'fry']

print(recipes)

# delete entry

del recipes['ketchup']

print(recipes)


# more dictionary methods

for key, value in recipes.items():
    print(f"{key} <<====>> {value}")

for key in recipes.keys():
    print(key)

for value in recipes.values():
    print(value)

list_recipe = list(recipes.keys())

print(list_recipe)

recipe_amount = list(recipes.values())

print(recipe_amount)

recipe_list_of_tuple = list(recipes.items())

print(recipe_list_of_tuple)


# get() method

get_bread = recipes.get('bread')

print(get_bread)

get_ketchup = recipes.get('ketchup', 'sorry no ketchup')
print(get_ketchup)

# update dictionary

more_recipes = {'pepper':True, 'garlic':1}

recipes.update(more_recipes)

print(recipes)

# pop a dictionary by key

recipes.pop('pepper')

recipes.pop('bread')

print(recipes)



# Movie Database

table = {
	'1975': 'Holy Grail',
	'1979': 'Life of Brian',
	'1983': 'The Meaning of Life',
	'2010': 'Inception'}

year = '2010'
movie_in_2010 = table[year]

print(movie_in_2010)

for year, movie in table.items():
    print(f"{movie} .......... {year}")

list_movies_year = list(table.items())
print(list_movies_year)



person = dict(name='bob', age=24)
print(person)
