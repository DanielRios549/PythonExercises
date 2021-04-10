'''
    Create a program that reads a number and show its double, triple and square root
'''

number = int(input('Type a number: '))

print(f'The double of {number} is {number * 2}')
print(f'The triple of {number} is {number * 3}')
print(f'The square root of {number} is {number  ** (1/2):.2f}')  # Square root could also be calculated with pow(number, 1/2)
