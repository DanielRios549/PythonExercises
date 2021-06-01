'''
    Get two values and show a menu on the screen.
    You need to run the selected operation.

    [1] Sum
    [2] Multiply
    [3] Higher
    [4] New numbers
    [5] Exit
'''

value1 = float(input('First Value: '))
value2 = float(input('Second Value: '))
print('What do you want to do? ')

optionText = '''
\033[34m[1]\033[m Sum
\033[34m[2]\033[m Multiply
\033[34m[3]\033[m Higher
\033[34m[4]\033[m New numbers
\033[34m[5]\033[m Exit

Choose an operation: '''

option = 0

while option != 5:
    option = int(input(optionText))

    if option != 5:
        if option == 4:
            value1 = float(input('First Value: '))
            value2 = float(input('Second Value: '))

        # Operations

        if option == 1:
            print(f'\033[34m{value1}\033[m + \033[34m{value2}\033[m equals \033[32m{value1 + value2:.2f}\033[m.')
        elif option == 2:
            print(f'\033[34m{value1}\033[m x \033[34m{value2}\033[m equals \033[32m{value1 * value2:.2f}\033[m.')
        elif option == 3:
            values = [value1, value2]
            print(f'The highest number you choose is \033[32m{max(values)}\033[m')
        else:
            print('\033[31mChoose a valid option, please.\033[m')
    else:
        print('Going out...')
