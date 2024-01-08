#### FILES AND EXCEPTIONS
from urllib.request import urlopen
# Reading from a file
from pathlib import Path
path = Path('/home/ubuntu2024/testme.txt')
# Reading the file
contents = path.read_text()
print(contents)
print(len(contents))
# We can use rstrip() on the contents string
contents = contents.rstrip()
print(contents)

# Accessing a file's lines
lines = contents.splitlines()
print(lines[2:5])
"""for line in lines:
    print(line)"""
    
# Working with a file's contents
file_string = ''
for line in lines:
    file_string += line
print(file_string)
print(len(file_string))

# Getting rid of whitespace
for line in lines:
    file_string += line.lstrip()
print(file_string[:100])
print(len(file_string))

# Wrting to a file
# Writing a single line

path = Path('/home/ubuntu2024/sample/programming.txt')
path.write_text('I love programming.')

# Writing multiple lines

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('/home/ubuntu2024/sample/programming.txt')
path.write_text(contents)

guests = input("Enter your full name: ")
path = Path('/home/ubuntu2024/sample/guests.txt')
path.write_text(guests)

### Exceptions
# handling the ZeroDivisionError exception
# division by zero
# using try-except blocks
try:
    print(10/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using exceptions to prevent crashes

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nEnter first number: ")
    if first_number == 'q':
        break
    second_number = input("\nEnter second number: ")
    if second_number == 'q':
        break
# The else block
# We can make this program more error resistant by wrapping the line that might produce errors in a try-except block.
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
        
# Handling the FileNotFoundError exception
# Let's try to read a file that doesn't exist
path = Path('/home/ubuntu2024/sample/testme.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, The file {path} doesn't exist.")

# Analyzing text

path = Path('/home/ubuntu2024/testme.txt')
# Reading the file
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, The file {path} doesn't exist.")
else:
# count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
    
web_path = ('https://ubuntu.com/')
# Reading the file
contents = urlopen(web_path)
print(contents)
html_bytes = contents.read()
html = html_bytes.decode('utf-8')
print(html)

# Working with multiple files
# we define a function
def count_words(path):
    # count the approximate number of words in the file:
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, The file {path} doesn't exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(words)
        print(f"The file {path} has about {num_words} words.")
        for word in words:
            print(word)
        
path = Path('/home/ubuntu2024/testme.txt')
count_words(path)

filenames = ['/home/ubuntu2024/testme.txt', '/home/ubuntu2024/important.txt', 'update.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
    
# Storing data