'''
    Remake the readInt() function from Exercise 104,
    adding the possibility of a invalid number.

    Also, create a readFloat() function with the same functionality.
'''
from utils.read import readInt, readFloat


integer = readInt('Type an \033[32mInteger\033[m number: ')
real = readFloat('Type a \033[32mReal\033[m number: ')

print('*' * 30)

print(f'The \033[32mInteger\033[m value is: \033[34m{integer}\033[m')
print(f'The \033[32mReal\033[m value is: \033[34m{real}\033[m')
