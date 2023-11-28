#!/usr/bin/env python3

# using the range function

age_under18 = range(18)

print(list(age_under18))

for age in list(age_under18):
    if age%2 ==0:
        print(age)
    print(age)


squares = []
for x in range(1,20):
    squares.append(x**2)
print(squares)

print(min(squares))

print(max(squares))

print(sum(squares))

# List Comphrension

age_even_under19 = [x for x in range(19) if x%2==0]
print(age_even_under19)

squares = [x**2 for x in range(1, 20)]
print(squares)

print(squares[2:7])

print(squares[-8:])

print(squares[4:12])


# looping through list

for square in squares[3:16]:
    print(square)
