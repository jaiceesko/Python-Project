#!/usr/bin/env python3

## FUNCTIONS

message = input("Hello, Please Tell me something.  ")

def messagee():
    print(message)

messagee()

messagee()

## Defining a function
# greeting user function

greeting = "Good day!"
def greet_user():
    print(greeting)
    print("Bonjour")

greet_user()

## Passing information to a function
# modify the function so it can greet the user by their names.

greeting = "Good day!"
def greet_user(username):
    print(f"{greeting} {username.title()}")
    print(f"Bonjour {username.title()}")

greet_user('zaira')
greet_user(input("what's your name?    "))


## Passing Arguments
# positional arguments

greeting = "Good day!"
def greet_user(name, surname):
    print(f"{greeting} {name.title()} {surname.title()}")
    print(f"Bonjour, {name.title()} {surname.title()}")

greet_user('zaira', 'dem')


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} is {pet_name.title()}.")

describe_pet('hamster' , 'harry')


## Keyword Arguments
greet_user(name='bintou', surname='dem')
describe_pet(animal_type='dog', pet_name='willie')


## Default Values
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} is {pet_name.title()}.")

describe_pet(pet_name='harry')
describe_pet('jerry')
describe_pet('juju', animal_type='hamster')


## return values
# The return statement takes a value from inside a function and sends it back
# to the line that called the function.

# making an argument optional

def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'seinfeld')
print(musician)


# making middle_name optional

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'seinfeld', 'maa')
print(musician)

musician = get_formatted_name('john', 'seinfeld')
print(musician)


## Returning a Dictionary

# The following function takes in parts of a name and returns a dictionary representing a person.

def build_person(first_name, last_name):
    person = {'first':first_name, 'last':last_name}
    return person

soldier = build_person('john', 'seinfeld')
print(soldier)


# extending this function to accept optional values

def build_person(first_name, last_name, age=None):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

soldier = build_person('john', 'seinfeld', 28)
print(soldier)

