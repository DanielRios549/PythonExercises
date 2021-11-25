'''
    Create a mini-system that use the Python interactive help system.
    The user will type the name of a module, and the help will be shown.
    If the user types 'q' or 'quit', the program will exit.
'''

from time import sleep


def message(text: str):
    width = 40
    print('\033[34m*\033[m' * width)
    print(f'\033[32m{text:^{width}}\033[m')
    print('\033[34m*\033[m' * width)


def PyHelp(command: str):
    message(f'Accessing {command} manual...')
    sleep(2)
    help(command)


message('PyHelp - Interactive Help System')

while True:
    print('Type \033[32mQ\033[m to exit from the manual and PyHelp.')
    package = input('Type the name of a package: ').lower()

    if package in ['q', 'quit']:
        break
    else:
        PyHelp(package)
