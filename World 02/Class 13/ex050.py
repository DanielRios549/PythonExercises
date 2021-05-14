'''
    Get 6 integer numbers and show the sum of the even ones. Do not consider the odd ones.
'''
sum_number = 0

for count in range(0, 6):
    number = int(input('Choose a number: '))

    if number % 2 == 0:
        sum_number += number

print(f'The sum of all even numbers equals {sum_number}')
