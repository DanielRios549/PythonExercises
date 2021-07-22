'''
    Get an undefined numbers of items and put them in a list.
    After that, create two extra lists, containing only odd and even values.

    In the end, show the three lists.
'''

numbers = []

while True:
    number = int(input('Choose a number: '))
    numbers.append(number)

    again = input('Do you want to continue? [Y/N] ').strip().upper()

    if again == 'N':
        break

odd = []
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f'You choose the following number: {numbers}')
print(f'The even ones are: {even}')
print(f'The odd ones are: {odd}')
