'''
    Get two integer numbers and compare them, showing the message:

    The first is higher.
    The second is higher.
    There is no higher number, both are the same.
'''
number01 = int(input('Choose a number: '))
number02 = int(input('Choose another number: '))

if number01 > number02:
    high = '\033[34mFirst\033[m'
elif number01 < number02:
    high = '\033[34mSecond\033[m'
else:
    high = False

if high is not False:
    print(f'The {high} is the higher.')
else:
    print(f'There is no higher number, both are the same.')
