'''
    Get four values from the user, and put them in a tuple.
    After that show the following:

    1 - How many times the number 9 appears.
    2 - In which position appears the number 3 for the first time.
    3 - The even numbers.
'''

values = []  # Like the previous exercise, this is better using a list.
even = []

for count in range(0, 4):
    number = int(input('Choose a number: '))
    values.append(number)

    if number % 2 == 0:
        even.append(number)

values = tuple(values)
even = tuple(even)

print(f'The number you chose are {values}')
print(f'The number 9 appears \033[34m{values.count(9)}\033[m times')
print(f'The number 3 appears in the index \033[34m{values.index(3)}\033[m for the first time')
print(f'The even numbers are {even}')
