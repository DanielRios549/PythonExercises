'''
    Modify the functions of exercise 107, adding a parameter that specify
    if the value returned by them will be formmated or not, using the function from exercise 108.
'''
import coin

number = float(input('Choose a price: R$ '))

print(f'The half of \033[34m{coin.format(number)}\033[m is \033[32m{coin.half(number, True)}\033[m')
print(f'The double of \033[34m{coin.format(number)}\033[m is \033[32m{coin.double(number, True)}\033[m')
print(f'Increasing \033[34m10%\033[m, the new price is \033[32m{coin.increment(number, 10, True)}\033[m')
print(f'Decreasing \033[34m35%\033[m, the new price is \033[32m{coin.decrement(number, 35, True)}\033[m')
