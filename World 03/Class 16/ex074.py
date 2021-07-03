'''
    Generate 5 random numbers and put them in a tuple.
    After that, show the generated numbers and show the lowest and the highest.
'''
from random import randint

numbers = []  # This is a problem better resolved using lists instead of tuples

# Another way to resolve this is using the following:
# numbers = tuple(randint(1, 1000) for count in range(0, 5))

for count in range(0, 5):
    numbers.append(randint(1, 1000))

numbers = tuple(numbers)  # After creating the list, convert it to a tuple to make it immutable.

print(f'The generated numbers are {numbers}')
print(f'The lowest is \033[34m{min(numbers)}\033[m and the highest is \033[34m{max(numbers)}\033[m')
