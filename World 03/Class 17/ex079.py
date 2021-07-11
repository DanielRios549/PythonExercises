'''
    Get an undefined numbers of values and put them in a list.
    In the end, show all the unique values in ascendent order.
'''
values = []

while True:
    number = int(input('Choose a number: '))

    if number not in values:
        print(f'\033[32mAdd the number {number} to the list.\033[m')
        values.append(number)
    else:
        print(f'\033[31mThe number {number} already exists in the list. Not added.\033[m')

    again = input('Do you want to continue? [Y/N]').upper()

    if again == 'N':
        break

values.sort()
print(f'You choose the values {values}')
