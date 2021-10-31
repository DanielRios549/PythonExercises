'''
    Create a function called 'factorial' that takes two parameters.
    The first is a number to calculate the factorial of.
    And the second is a optional boolean to determinate if the factorial will be displayed.

    Add the Docstring as well.
'''


def factorial(number: int, show=False):
    '''
        Calculate the factorial of a number

        :param number: integer positive number to calculate
        :param show: boolean to show the calculation or not. Default is not.
    '''
    result = 1

    print(f'{number}!', end=' ')

    for current in range(number, 0, -1):
        result *= current

        if show is True:
            print(f'\033[34m{current}\033[m ', end='')

            if current > 1:
                print('x ', end='')
            else:
                print('', end='')

    print(f'= \033[32m{result}\033[m')


factorial(
    int(input('Choose a number to see it\'s factorial: ')),
    False
)
