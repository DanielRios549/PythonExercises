'''
    Create a module called coin.py with the following functions:
    increment(), decrement(), double() and half()

    Also create a program to import and use some of these functions.
'''
import coin

number = int(input('Choose a price: R$ '))

print(f'The half of \033[34m{number}\033[m is \033[32m{coin.half(number)}\033[m')
print(f'The double of \033[34m{number}\033[m is \033[32m{coin.double(number)}\033[m')
print(f'Increasing \033[34m10%\033[m, the new price is \033[32m{coin.increment(number, 10)}\033[m')
print(f'Decreasing \033[34m35%\033[m, the new price is \033[32m{coin.decrement(number, 35)}\033[m')
