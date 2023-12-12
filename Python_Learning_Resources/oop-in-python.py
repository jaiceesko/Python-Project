## OOP in Python

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
    def fill_gas_tank(self):
        print("This car does have a gas tank!")


# Instances

car1 = Car('audi', 'a4', '2022')
print(car1.get_descriptive_name())
print(car1.odometer_reading)
print(car1.make)


car2 = Car('wami', 'w18', '2023')
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

# Instances as Attributes
class Battery:
    def __init__(self, battery_size=40):
# Initialize the battery's attributes.
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")
# Add another method to battery that reports the range of the car based on battery size.

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
            
        print(f"This car can go about {range} miles on a full charge.")

# Inheritance

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
# Defining attributes and methods for the child class
    #def describe_battery(self):
        #print(f"This {self.make.title()} car has a {self.battery_size}-KWh battery.")
# Overriding methods from the parent class
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")


    
my_leaf = ElectricCar('tesla', 't18', '2022')
print(my_leaf.get_descriptive_name())
#my_leaf.describe_battery()
battery1 = Battery(65)
battery1.describe_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()