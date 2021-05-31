'''
    Get a number and show its factorial.

    For version.
'''

number = int(input('Choose a number: '))
result = 1

for count in range(number, 0, -1):
    result *= count

    if count > 1:
        print(f'\033[34m{count}\033[m x ', end='')
    else:
        print(f'\033[34m{count}\033[m = \033[32m{result}\033[m')
