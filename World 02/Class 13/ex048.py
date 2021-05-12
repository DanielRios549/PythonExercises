'''
    Sum all the odd numbers multiples of 3 between 1 and 500
'''
numbers_summed = 0
numbers_shown = 0

for count in range(3, 500, 6):
    numbers_summed += count
    numbers_shown += 1

print(f'The sum of all \033[34m{numbers_shown}\033[m requested numbers equals \033[32m{numbers_summed}\033[m')
