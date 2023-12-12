#!/usr/bin/env python3

# class employee

class Employee:
# class variable
    raise_amt = 1.04

# defining instance
    def __init__(self, first, last, pay):
# instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@fenix.co"

# instance method

    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"

    def set_raise(self):
        self.pay = int(self.pay) * self.raise_amount

# Creating subclasses
class Developer(Employee):
    raise_amt = 1.95
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print(emp.fullname())






# object

emp_1 = Employee('zaira' , 'jobe', 40000)
emp_2 = Employee('sara', 'jallow', 50000)

emp_3 = Developer('samba', 'samba', 60000, 'python')
emp_4 = Developer('titi', 'zuri', 70000, 'java')

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_3.fullname())
print(emp_4.prog_lang)

mgr_1 = Manager('shelly', 'rami', 90000, [emp_1, emp_2])
print(mgr_1.print_employee())
mgr_1.add_employee(emp_4)

mgr_1.print_employee()
