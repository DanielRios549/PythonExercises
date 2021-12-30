'''
    Create a mini modular system that allows register people with name and age in a text file.
    The system will have two options:

    1 - Register a new person.
    2 - Show all registered people.
'''
import utils.menu as menu
import utils.colors as color

option = menu.create('Main Menu', 30)

print(f'Your Option is: {color.green(option)}')
