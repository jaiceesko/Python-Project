#!/usr/bin/env python3

### FUNCTIONS

## Adding a new optional parameter to the function definition

def build_person(first_name, last_name, age=None):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

soldier = build_person('john', 'seinfeld', 28)
print(soldier)

## Using a function with a while loop

# let's use the get_formatted_name() function with a while loop

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# while loop

prompt = input("\nPlease tell me your name: ")
while prompt !='quit':
    f_name = input("First name: ")
    if f_name =='q' or f_name =='quit':
        break
    l_name = input("Last name: ")
    if l_name =='q' or l_name =='quit':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    

## Passing a List
# the function grrets each person in the list individually.

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'yassin', 'ty']
greet_users(usernames)


## Modifying a list in a function

def print_models(unprinted_designs, completed_models):

# simulate printing each design, until none are left.
# move each design to completed_models after printing.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'rebot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
   

## Passing an arbitrary number of arguments

def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pepper', 'extra cheese')


## Mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



## Using arbitrary keyword arguments

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile1 = build_profile('albert', 'seinfeld', 'age'=30)
user_profile2 = build_profile('zaira', 'jobe', 'location'='Banjul', 'age'=25)

