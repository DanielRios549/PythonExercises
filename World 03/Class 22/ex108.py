'''
    Adapt the code in exercise 107, creating an additional function called format()
    that shows the money values formmated.
'''
import coin

number = float(input('Choose a price: R$ '))

print(f'The half of \033[34m{coin.format(number)}\033[m is \033[32m{coin.format(coin.half(number))}\033[m')
print(f'The double of \033[34m{coin.format(number)}\033[m is \033[32m{coin.format(coin.double(number))}\033[m')
print(f'Increasing \033[34m10%\033[m, the new price is \033[32m{coin.format(coin.increment(number, 10))}\033[m')
print(f'Decreasing \033[34m35%\033[m, the new price is \033[32m{coin.format(coin.decrement(number, 35))}\033[m')
