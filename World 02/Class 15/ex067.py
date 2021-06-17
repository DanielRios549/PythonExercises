'''
    Show the multiplication table of various numbers.
    The program should stops if the number was negative.
'''

number = 0

while True:
    number = int(input('Choose a number shot its multiplication table: '))

    if number < 0:
        break

    count = 1
    while count <= 10:
        print(f'\033[34m{number}\033[m x \033[34m{count:>2}\033[m = \033[32m{number * count}\033[m')
        count += 1

print(f'Program finished...')
