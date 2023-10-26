#!/usr/bin/env python3

# If Statements Conditionals

cars = ['audi', 'tesla', 'bmw', 'subaru', 'toyota', 'mercedes']
for i  in cars:
    if i=='tesla' or i=='audi':
        print(i.upper())
    else:
        print(i.title())
    print('That"s a nice ' + i)


name = 'seinfeld'

print(name=='Seinfeld')

print(name.title()=='Seinfeld')


not_squares = [x**2 for x in range(20) if x%2!=0]

print(not_squares)


comedies = ['seinfeld', 'elaine', 'kramer', 'george', 'puddy', 'mike', 'karen', 'tida']

for comedy in comedies:
    if comedy=='tida' or comedy=='mike':
        print('Hey, You were not part of seinfeld sitcom')
    else:
        print(comedy)


age = 19

if age >=18:
    print('You are old enough to vote!')


weight_kg = 90
height_meter = 1.60

bmi =  weight_kg/height_meter**2

if bmi <=17:
    print("you are underweight")

elif bmi >=18 and bmi<=28:
    print("You have great weight")

else:
    print("Your bmi is above the healthy range")





weight_kg = int(input("Hello, What's your weight in kg? \n"))

height_cm = int(input("Hello, What's your height in cm? \n"))/100

bmi = weight_kg/height_cm**2

print(bmi)


if bmi <=18:
    print('please gain some weight. You are underweight')

elif 19 <= bmi <=27:
    print("Your BMI is good. keep the good work!")

else:
    print('please you are overweight')


