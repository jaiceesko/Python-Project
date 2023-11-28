#!/usr/bin/env python3

# User Input and While Loops


count = 0
while count <=10:
    print('meow')
    count +=1


i = 3
while i !=0:
    print("Hello World")
    i-=1
print('Time to start count')

count = 0

while count <=4:
    count +=1
    if count ==1:
        print(f"you have {count} set")
    else:
        print(f"you have {count} sets")
print('Finish your training sets.')


# working with float

num = 1
while num <10:
    print('keep counting')
    num+=.1
    num = round(num, 1)
    print(num)
print('Finish counting')



# how the input() function works

#message = input('What is your name? \n')
#print (message)

message = input('Tell me something, and I will repeat it back to you:  ')

while message != 'quit':
    name = input('Please, What is your name?  ')
    if name =='quit' or name=='q':
        break
    else:
        print(name)
print('See you again!')


# using int() to accept numerical input

age = input("How old are you?     ")

age = int(age)
print(age)

if age > 24:
    print('Hello')
else:
    print('hi')

message = ""
while message !='quit':
    message = input('\nTell me something, and I will repeat it back to you: \nEnter "quit" to end the program.')
    if message =='quit' or message=='q':
        break
    else:
        print(message)

# Using a flag

active = True
while active:
    message = input("Hey, What's your favorite comedy of all time?  ")

    if message =='quit' or message=='q':
        active = False
    elif message == 'waka':
        active=False
    else:
        print(message)

# Using continue in a loop
# a loop that counts from 1 to 10 but prints only the odd numbers

current_number = 0
while current_number <=10:
    current_number +=1
    if current_number % 2 ==0:
        continue
    print(current_number)


# using a while loop with lists and dictionaries

# to modify a list as you work through it, use a while loop.

# moving items from one list to another

# start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'zaira', 'maria', 'okurri', 'mat', 'sohna']
confirmed_users = []

# verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    
    confirmed_users.append(current_user)

# display all confirmed users

print("\nThe following users have been confirmed:")
print(confirmed_users)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# sandwich orders

sandwich_orders = ["chicken sandwich", "egg sandwich","seafood sandwich","vegan sandwich", "classic sandwich"]
finished_sandwiches = []

while sandwich_orders:
    finish_order = sandwich_orders.pop()
    print(f"I made your {finish_order}")
    finished_sandwiches.append(finish_order)
    
print(finished_sandwiches)
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


## Removing All Instances of specific values from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    

print(pets)
    

# filling a dictionary with user input
# we wants to connect each response with a participant

responses = {}

# set a flag to indicate that polling is active.
polling_active = True

while polling_active:
# prompt for the person's name and response.
    name = input("\nWhat is your name?   ")
    response = input("Which country would you like to travel someday?   ")

# store the response in the dictionary
    responses[name] = response
# find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond?  (yes/no) ")
    if repeat == 'no' or repeat=='No':
        polling_active = False

# polling is complete. show the results.
print(responses)
print("\n----------Poll Results----------")
for name, response in responses.items():
    print(f"{name.title()} -------{response.title()}.")

