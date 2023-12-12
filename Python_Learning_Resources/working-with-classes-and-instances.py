#!/usr/bin/env python3

### Working With Classes and Instances


# The Car Class

class Car:
    def __init__(self, make, model, year):
# Initialize attributes to describe a car.
# Instance variable
        self.make = make
        self.model = model
        self.year = year
# Setting a Default value for an attribute
        self.odometer_reading = 0
# method
    def get_descriptive_name(self):
        long_name = f"{self.make.title()} {self.model.title()} {self.year}"
        return long_name
# Print a statement showing the car's mileage.
    def read_odometer(self):
        print(f"This {self.make.title()} {self.model.title()} car has {self.odometer_reading} miles on it.")
# Modifying an attribute's value through a method
    def update_odometer(self, mileage):
# set the odometer reading to the given value.
        self.odometer_reading = mileage

# Incrementing an attribute's value through a method
    def increment_odometer(self, miles):
# Add the given amount to the odometer reading
        self.odometer_reading += miles



# Instances

car1 = Car('audi', 'a4', '2022')
print(car1.get_descriptive_name())
print(car1.odometer_reading)
print(car1.make)


car2 = Car('tesla', 't18', '2023')
print(car2.get_descriptive_name())
car2.read_odometer()

# Modifying an attribute's value directly

car1.odometer_reading = 23
car1.read_odometer()

# modifying an attribute value through method

car2.update_odometer(30)
car2.read_odometer()

car1.update_odometer(60)
car1.read_odometer()

# increment mile

car1.increment_odometer(100)
car1.read_odometer()



#### Class Variables


class Employee:
# class variable
    num_of_emps = 0
    raise_amount = 600

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
# instance variable
        self.pay_minimum = 800
        self.email = f"{fname}.{lname}@fenix.com"
# incrementing the number of employees whenever an instance is created
        Employee.num_of_emps +=1

    def fullname(self):
        return f"{self.fname.title()} {self.lname.title()}"

    def apply_raise(self, salary):
        self.pay_minimum = salary * 1.04
        return self.pay_minimum

    def raise_apply(self, salary):
        self.pay_minimum = salary + self.raise_amount
        return self.pay_minimum


print(Employee.raise_amount)

print(Employee.__dict__)

emp_1 = Employee('zaira', 'lowe')
print(emp_1.fullname())
print(emp_1.email)

print(emp_1.__dict__)

print(emp_1.pay_minimum)
print(emp_1.apply_raise(2000))


emp_2 = Employee('sara', 'jallow')
print(emp_2.apply_raise(2000))
print(emp_2.raise_apply(2000))

emp_2.raise_amount = 800
print(emp_2.raise_apply(3000))

print(Employee.num_of_emps)
