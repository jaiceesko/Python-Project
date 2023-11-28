#!/usr/bin/env python3

# Tuples


names = ('zaina', 'skaima')

print(names)

print(names[1])

for name in names:
    print(name)

# will produce an error you cannot change an entry

# names[1] = 'jallow'

squares = [x**2 for x in range(10)]

squares = tuple(squares)

print(type(squares))

print(squares)

print(squares[2:7])

t= tuple('lupins')

for i in t:
    print(i)
