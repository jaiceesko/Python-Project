#!/usr/bin/env python3

## CLASSES IN PYTHON

## Classes allow us logically to group our data and functions in a way that's
## easy to reuse and also easy to build upon if need be 


## Classes and Instances


class Employee:
    def __init__(self, fname, lname, salary, dept):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.dept = dept
        self.email = f"{fname}.{lname}@fenix.com"

# methods
    def emp_description(self):
        return f"{self.fname.title()} {self.lname.title()}"
    def emp_email(self):
        emp_info = self.dept + ' ' + self.email
        return emp_info
    def emp_salary(self):
        return f"{self.fname.title()} {self.lname.title()}...... Salary: ${self.salary}"



# Instances

emp_zaira = Employee('zaira', 'jallow', 40000, 'marketing')


print(emp_zaira.fname)
print(emp_zaira.lname)
print(emp_zaira.dept)
print(emp_zaira.email, '  ', emp_zaira.salary)
print(emp_zaira.emp_description())
print(emp_zaira.emp_email())
print(emp_zaira.emp_salary())

emp_joe = Employee('joe', 'mbow', 50000, 'IT')

print(emp_joe.emp_description())
print(emp_joe.emp_email())
print(emp_joe.emp_salary())

emp_sara = Employee('sara', 'mbye', 40000, 'sale')

print(emp_sara.emp_description())
print(emp_sara.emp_email())
print(emp_sara.emp_salary())


## Creating the Dog Class

class Dog:

# A function that's part of a class is a method.
    def __init__(self, name, age):
# Initialize name and age attributes.
        self.name = name
        self.age = age

    def sit(self):
# Simulate a dog sitting in response to a command.
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
# Simulate rolling over in response to a command.
        print(f"{self.name.title()} rolled over!")

# Making an instance from a class
dog1 = Dog('chuchu', 2)

print(dog1.name)
print(dog1.age)

dog1.sit()
dog1.roll_over()

dog2 = Dog('titi', 1)

print(f"{dog2.name} {dog2.age}")
dog2.sit()
dog2.roll_over()
