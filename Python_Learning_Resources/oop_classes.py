#!/usr/bin/env python3

## Object Oriented Programming in Python





class  Country:
    language = ''
    num_of_country = 0
    def __init__(self, name, capital, continent):
        self.name = name
        self.capital = capital
        self.continent = continent
        Country.num_of_country += 1
    def country_detail(self):
        country = f"{self.name} {self.capital}"
        return country.title()

    def get_continent(self):
        print(self.continent.title())

    def set_language(self, lang):
        self.language = lang
        return self.language

country1 = Country('kenya', 'nairobi', 'africa')
print(country1.country_detail())
country1.get_continent()
country2 = Country('poland', 'warsaw', 'europe')
print(country2.set_language('polish'))


print(Country.num_of_country)


class Student:
    school = 'Fenix High'
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
# we would add student to a course
class SemesterCourse:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
    
    
    
s1 = Student('zaira', 19, 96)
s2 = Student('sara', 19, 70)
s3 = Student('bintou', 19,80)
    
course_1= SemesterCourse('science', 2)
course_1.add_student(s1)
course_1.add_student(s2)
course_1.add_student(s3)

print(course_1.students[0].name)
print(course_1.get_average_grade())


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name.title()}.....Cuisine Type: {self.cuisine_type.title()}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")
        
    def set_served(self, num_of_client):
        self.number_served = num_of_client
        return f"{self.restaurant_name.title()} Restaurant serve {self.number_served} clients today."
    def increment_set_served(self, extra_num_of_client):
        self.number_served += extra_num_of_client
        return f"{self.restaurant_name.title()} Restaurant serve {self.number_served} clients today."
        
        
kam_restaurant = Restaurant('Kami', 'Indian')
kam_restaurant.describe_restaurant()
kam_restaurant.open_restaurant()
print(kam_restaurant.set_served(10))
print(kam_restaurant.increment_set_served(20))

zara_restaurant = Restaurant('Belle', 'french')
zara_restaurant.describe_restaurant()
zara_restaurant.open_restaurant()



class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} ")
        
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}")
        
user1 = Users('zara', 'jallow')
user1.describe_user()
user1.greet_user()

user2 = Users('bintou', 'jobe')
user2.describe_user()
user2.greet_user()