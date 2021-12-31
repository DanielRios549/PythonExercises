from time import sleep
import utils.colors as color
import utils.show as show
import utils.read as read
import utils.people.actions as people

optionsList = [
    'View Registered People',
    'Register Another Person',
    'Exit'
]


def options():
    print('\n')

    for index, item in enumerate(optionsList):
        print(f'{color.yellow(index + 1)} - {color.blue(item)}')

    print('\n')

    valid = ''

    while valid not in optionsList:
        try:
            option = read.readInt('Your Option: ')

            if option == 0:
                option = 1

            exists = optionsList[option - 1]

        except IndexError:
            print(color.red('Choose a valid option, please.'))

        else:
            valid = exists

    return valid


def create(title: str, width: int = 0):
    if width == 0:
        width = len(title) + 4

    while True:
        show.header(title)

        option = options()

        if type(option) == str:
            if 'View' in option.split():
                people.list()

            elif 'Register' in option.split():
                name = read.readName('Name: ')
                age = read.readInt('Age: ')

                people.register(name, age)

            else:
                show.header('Exiting... Se you!')
                sleep(2)
                break

        else:
            print(color.red('Ops, there is a problem with the program...'))

    return option
