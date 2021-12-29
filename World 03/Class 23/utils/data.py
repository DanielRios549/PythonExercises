import utils.colors as color
from utils.read import readInt


def options():
    optionsList = [
        'View Registered People',
        'Register Another Person',
        'Exit'
    ]

    print('\n')

    for index, item in enumerate(optionsList):
        print(f'{color.yellow(index + 1)} - {color.blue(item)}')

    print('\n')

    valid = False

    while valid not in optionsList:
        try:
            option = readInt('Your Option: ')

            if option == 0:
                option = 1

            exists = optionsList[option - 1]

        except IndexError:
            print(color.red('Choose a valid option, please.'))

        else:
            valid = exists

    return valid


def menu(title: str, width: int = 0):
    separator = '-'

    if width == 0:
        width = len(title) + 4

    print(color.blue(separator * width))
    print(color.green(title.center(width)))
    print(color.blue(separator * width))

    option = options()

    return option
