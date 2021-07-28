'''
    Get seven numeric values and put then in a unique list with even and odd separately.
    In the end, show both even and odd values in increased order.
'''

numbers = [list(), list()]

for count in range(0, 7):
    number = int(input(f'Choose the {count + 1}º number: '))

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

numbers[0].sort()
numbers[1].sort()

print(f'The even numbers are: {numbers[0]}')
print(f'And the odd numbers are: {numbers[1]}')
