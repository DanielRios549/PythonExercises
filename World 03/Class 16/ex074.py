'''
    Generate 5 random numbers and put them in a tuple.
    After that, show the generated numbers and show the lowest and the highest.
'''
from random import randint

numbers = []  # This is a problem better resolved using lists instead of tuples

for count in range(0, 5):
    numbers.append(randint(1, 1000))

print(f'The generated numbers are {numbers}')
print(f'The lowest is {min(numbers)} and the highest is {max(numbers)}')
