'''
    Create a function called 'getInt' that works like the built-in function 'input'.
    The function should take only a integer as parameter.
'''


def readInt(text: str):
    number = input(text).strip()

    while number.isdigit() is not True:
        print('\033[31mError\033[m. Please choose a \033[32mvalid integer number\033[m.')
        number = input(text)

    return number


number = readInt('Type a number: ')
print(f'You just type the number \033[34m{number}\033[m')
