'''
    Get 5 values and put them in a list, respecting the ascendent order.
    In the end, show the list ordered.
'''

numbers = []

for count in range(0, 5):
    number = int(input('Choose a number: '))

    if count == 0 or number >= max(numbers):
        numbers.append(number)
        print('Adding in the end')
    elif number <= min(numbers):
        numbers.insert(0, number)
        print('Adding in the start')
    else:
        add = 0
        for index in range(0, len(numbers)):
            if number >= numbers[index]:
                add += 1
            else:
                break
        numbers.insert(add, number)
        print(f'Adding at the position {add}')

print(numbers)