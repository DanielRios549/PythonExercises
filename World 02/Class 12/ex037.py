'''
    Get an integer number and let the user decide what will be the convertion base:

    1 - Binary
    2 - Octal
    3 - Hexadecimal
'''
number = int(input('Choose a number: '))

convert = int(input('''
\033[34m1\033[m - Binary
\033[34m2\033[m - Octal
\033[34m3\033[m - Hexadecimal

What format do you want to convert it? '''))

if convert == 1:
    option = 'Binary'
    converted = bin(number)
elif convert == 2:
    option = 'Octal'
    converted = oct(number)
elif convert == 3:
    option = 'Hexadecimal'
    converted = hex(number)
else:
    option = False
    print('Choose a valid convert option, please.')

if option is not False:
    print(f'\033[33m{number}\033[m converted to \033[32m{option}\033[m is \033[35m{converted[2:]}\033[m.')
