'''
    Get an integer number and show if it is even or odd
'''
number = int(input('Type a number: '))

if number % 2 == 0:  # This is the mathematic way to calculate an even number
    print('The number is \033[32meven\033[m.')
else:
    print('The number is \033[31modd\033[m.')
