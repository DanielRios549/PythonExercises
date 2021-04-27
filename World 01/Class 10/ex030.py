'''
    Get an integer number and show if it is even or odd
'''
number = int(input('Type a number: '))

if number % 2 == 0:  # This is the mathematic way to calculate an even number
    print('The number is even.')
else:
    print('The number is odd.')
