'''
    Get an integer number and show the firsts items in a Fibonacci Sequence.
'''

sequence = int(input('How many numbers do you want to show? '))
operand1 = 0
operand2 = 1
count = 1

while count <= sequence:
    result = operand1 + operand2

    if count < sequence:
        if count % 10 == 0:
            print(f'\033[32m{result}\033[m')
        else:
            print(f'\033[32m{result}\033[m', end=' -> ')
    else:
        print(f'\033[32m{result}\033[m')

    operand1 = operand2
    operand2 = result
    count += 1
