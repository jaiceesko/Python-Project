#!/usr/bin/env python3

# Strings

print("Hello World")

name = 'Jainaba'

print(name)


# String Methods

message = "one of python's strengths is its diverse and supportive community"

print(message)

print(message.title())

print(message.upper())

print(type(message))

print(message.find("diverse"))

print(message.index("and"))


# Adding Whitespaces to Strings with Tabs or Newlines

languages = "\n\tPython \n\tRust \n\tJavascript"
print(languages)


funny_text = "     Monday and Sunday    "

print(funny_text.lstrip())

print(funny_text.rstrip())

print(funny_text.strip())
