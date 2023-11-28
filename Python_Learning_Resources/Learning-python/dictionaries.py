#!/usr/bin/env python3

### DICTIONARIES

details = {'name':'zaira', 'age':26, 'university':'BDCS', 'country':'senegal'}

print(details)

get_university = details.get('university')

print(get_university)


for i,v in details.items():
    print(f"{i}  : {v}")

alien_0 = {'color':'green', 'points':5}

# accessing values in a dictionary

print(alien_0['color'])

print(alien_0['points'])

# adding new key-value pairs

alien_0['position']=2

print(alien_0['position'])

print(alien_0)

# starting with an empty dictionary

aliens = {}

aliens['name'] = 'tarzan'

aliens['position'] = 1

aliens['color'] = 'red'

aliens['x_position'] = 0

aliens['y_position'] = 25

print(aliens)

# modifying values in a dictionary

aliens['color'] = 'yellow'

print(aliens)

aliens['speed'] = 'medium'

print(aliens)

# move the alien to the right
# determine how far to move the alien based on its current speed.

if aliens['speed'] == 'slow':
    x_increment = 1

elif aliens['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

aliens['x_position'] = aliens['x_position'] + x_increment

print(aliens['x_position'])


# removing key-value pairs

del aliens['color']

print(aliens)

# using get() to access values

print(aliens.get('speed'))


student = {'name':'John', 'age':25, 'courses':['Math', 'Physics', "Computer Science"]}

print(student)

print(student['courses'][1:])

print(student.get('name'))


#  looping through key-pairs

for key,value in student.items():
    print(f"{key} ====>>> {value}")

# looping through keys
for key in student.keys():
    print(key)

# looping through values

for value in student.values():
    print(value)



## Nesting

# A list of Dictionaries

user_1 = {'name':'joe', 'username':'joeki1'}
user_2 = {'name':'zaira', 'username':'zaihaha4'}
user_3 = {'name':'baila', 'username':'ball83'}

users = [user_1, user_2, user_3]

for user in users:
    print(user)

# game of aliens

# make an empty lists
aliens = []

# make 20 aliens

for alien_number in  range(20):
    new_alien = {'name':'zumba', 'color':'red', 'points':15, 'speed':'fast'}
    aliens.append(new_alien)

print(aliens[:6])

print(len(aliens))

for alien in aliens[:6]:
    if alien['name'] == 'zumba':
        alien['name'] = 'zadna'
        alien['color'] = 'blue'
        alien['points'] = 10
        alien['speed'] = 'medium'

print(aliens[:6])


# A list in a dictionary

student = {'name':'sally', 'subjects':['python', 'information security', 'physics']}

for key,value in student.items():
    print(key, value)

favorite_languages = {
	'jen':['python', 'rust'],
	'sarah':['c', 'c#'],
	'edward':['rust', 'go'],
	'phil':['python', 'haskell']}
print(favorite_languages)

for name, languages in favorite_languages.items():
    print(name, languages)
    for language in languages:
        print(language.title())
