'''
    Get various integer numbers. In the end, show the average between all values and the lowest and the highest.
    Asks the user if they want to continue or not.
'''
number = int(input('Choose a number: '))
again = input('Do you want to continue? [S/N]').strip().upper()
total = 1
maximum = number
minimum = number

while again == 'S':
    number2 = int(input('Choose another number: '))
    total += 1
    number += number2
    again = input('Do you want to continue? [S/N]').strip().upper()

    if number2 > maximum:
        maximum = number2
    elif number2 < minimum:
        minimum = number2

print(f'The average of these \033[34m{total}\033[m number is \033[34m{number / total:.2f}\033[m.')
print(f'The highest is \033[34m{maximum}\033[m, and the lowest is \033[34m{minimum}\033[m.')
