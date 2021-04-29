'''
    Get a number and show it integer part
'''
from math import trunc

number = float(input('Type a number: '))
print(f'The integer part of \033[34m{number} \033[mis \033[32m{trunc(number)}\033[m')
