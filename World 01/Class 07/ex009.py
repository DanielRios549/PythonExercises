'''
    Create a program that reads a number and show its multiplication table
'''
number = int(input('Type a number: '))

print('-' * 12)
print(f'\033[34m{number}\033[m x \033[34m{1:>2}\033[m = \033[32m{number * 1}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{2:>2}\033[m = \033[32m{number * 2}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{3:>2}\033[m = \033[32m{number * 3}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{4:>2}\033[m = \033[32m{number * 4}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{5:>2}\033[m = \033[32m{number * 5}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{6:>2}\033[m = \033[32m{number * 6}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{7:>2}\033[m = \033[32m{number * 7}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{8:>2}\033[m = \033[32m{number * 8}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{9:>2}\033[m = \033[32m{number * 9}\033[m')
print(f'\033[34m{number}\033[m x \033[34m{10}\033[m = \033[32m{number * 10}\033[m')
print('-' * 12)
