#!/usr/bin/env python3

### Class methods and Static methods

class Student:
    university = "Fenix University"
    num_of_student = 0
    def __init__(self, name, major,year):
        self.name = name
        self.major = major
        self.year = year
        graduation_year = ''
        
        Student.num_of_student +=1
        
    def get_student_detail(self):
        full_info = f"{self.name} {self.major} {self.year}"
        return full_info.title()

    def get_graduation_year(self, graduation):
        self.graduation_year = graduation
        return self.graduation_year

    @classmethod
    def get_school(cls):
        return Student.university

    @staticmethod
    def get_grade(grade):
        print(grade)




student1 = Student('zaira', 'computer science', '2017')
print(student1.get_student_detail())
print(student1.get_graduation_year(2021))
print(Student.get_school())

print(student1.get_school())

student1.get_grade(80)

student2 = Student('sara', 'economics', '2020')
student3 = Student('joe', 'mathematics', '2021')
student4 = Student('kamala', 'law', '2022')

print(Student.num_of_student)


class Employee:

# class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
# instance variable
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f"{fname}.{lname}@fenix.org"
        Employee.num_of_emps += 1

# instance method
    def get_full_detail(self):
        return f"{self.fname.title()} {self.lname.title()} {self.email}"

    def set_raise(self):
        self.pay = int(self.pay) * self.raise_amount
        return self.pay

# class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        return cls.raise_amount
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
# create new object
        return cls(fname, lname, pay)


emp1 = Employee('zaira', 'jobe', '24000')
print(emp1.get_full_detail())
print(emp1.set_raise())

emp2 = Employee('sara', 'jallow', '26000')


print(Employee.set_raise_amount(1.95))
print(emp1.raise_amount)
print(emp2.raise_amount)


emp_str_1 = 'John-Cafe-40000'
emp_str_2 = 'Bintou-Mbir-50000'

emp3 = Employee.from_string(emp_str_1)
print(emp3.get_full_detail())

emp4 = Employee.from_string(emp_str_2)
print(emp4.get_full_detail())
