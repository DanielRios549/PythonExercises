'''
    Get a number and show it integer part
'''
from math import trunc

number = float(input('Type a number: '))
print(f'The integer part of {number} is {trunc(number)}')
