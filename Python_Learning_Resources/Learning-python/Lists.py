#!/usr/bin/env python3

# Lists

countries = ["gambia", "poland", "slovakia", "malta", "italy", "mauritius", "kenya"]

print(countries)

european_countries = countries[1:5]
print(european_countries)

print(countries[0])

for country in countries:
    print(country.title())


names = ["sheinfeld", "elaine", "kramer","george", "puddy"]

print(names)

print(names[:-1])

print(names[2])

identities = ["zaina", 26, 'eritrean', "sales", 64, "hiking", "malta"]

print(identities)

print(identities[-5:-1])


# Modifying, Adding, and Removing Elements

countries[4] = "austria"

print(countries)

names.append('sara')

print(names)


identities.insert(3, "Bachelor Degree")

print(identities)


identities.remove("sales")

print(identities)

name_pop = names.pop()

print(name_pop)

del countries[1:3]

print(countries)


# Organizing a List

names.sort()

print(names)

sorted_countries = sorted(countries)

print(sorted_countries)

european_countries.reverse()

print(european_countries)

print(f"{len(identities)}  : {len(names)}")
