'''
    Remake the exercise 009, showing the multiplication table of a number,
    now using a for loop.
'''
number = int(input('Choose a number: '))

for count in range(1, 11):
    print(f'\033[34m{number}\033[m x \033[34m{count:>2}\033[m = \033[32m{number * count}\033[m')
