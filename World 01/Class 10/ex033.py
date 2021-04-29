'''
    Get three numbers and show how is the highest and how is the lowest.
'''

number1 = int(input('First number: '))
number2 = int(input('Second number: '))
number3 = int(input('Third number: '))

if number1 == number2 and number3:
    print('\033[31mChoose different number, please.\033[m')
else:
    numbers = [number1, number2, number3]

# The empty lines in following print is for the text doesn't stay stuck in the inputs

print(f'''

The lowest number was \033[31m{min(numbers)}\033[m
The Highest number was \033[32m{max(numbers)}\033[m
''')
