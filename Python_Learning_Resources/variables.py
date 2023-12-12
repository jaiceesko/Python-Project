#!/usr/bin/env python3

# Variables

# strings
fullname = input("What is your name?\n")
country = input("Enter your country name.  ")

print(f"{fullname.title()} ----->>>>> {country.title()}")
name = "Jainara"
print(name)

age = input("Enter your age.   ")
print(type(age))

# Integer

print(int(age))
age = 26
print(age)

hours_sleep = input('Enter hours of sleep.  ')
print(int(hours_sleep))

yearly_bonus = 800
balance = input("Enter your current balance.  ")
total_balance = yearly_bonus + int(balance)
print(total_balance)

num1 = input('Pick Your favorite number:  ')

num2 = input("Pick Your least favorite number:  ")

sum  = int(num1) + int(num2)
print(sum)

print(int(num1) >= int(num2))
# Boolean

is_female = True
print(is_female)

fruit = 'banana'
spice = 'paprika'

print(fruit == spice)

favorite = 'banana'

print(fruit == favorite)

# Float

weight = 62.5
print(weight)
print(type(weight))

odd = 45 / 6
print(odd)
