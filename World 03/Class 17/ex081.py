'''
    Get an undefined numbers of values and put them in a list.
    After that, show the following:

    1 - How many items the user choose.
    2 - The list ordered by decreased order.
    3 - If the value 5 was chosen and if it is or not in the list.
'''
numbers = []

while True:
    numbers.append(int(input('Choose a number: ')))

    again = input('Do you want to continue? [Y/N] ').strip().upper()

    if again == 'N':
        break

numbers.sort(reverse=True)
print(f'You choose \033[34m{len(numbers)}\033[m values.')
print(f'The values in decreased order are {numbers}')
print('The value 5 {} the list'.format('\033[32mis inside\033[m' if 5 in numbers else '\033[31mis not inside\033[m'))
