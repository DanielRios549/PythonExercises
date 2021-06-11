'''
    Get various integer numbers. The loop will only stops when the user choose 999, this is the stop condition.
    In the end show how many numbers they choose and show the sum between them, except from the flag.
'''
number = int(input('Choose a number: [999 to exit] '))
total = 0
sum = 0

while number != 999:
    total += 1
    sum += number
    number = int(input('Choose another number: [999 to exit] '))

print(f'You chose \033[34m{total}\033[m numbers and the sum between them equals \033[34m{sum}\033[m.')
