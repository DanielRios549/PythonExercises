'''
    Create a program that reads a number and show its double, triple and square root
'''

number = int(input('Type a number: '))

print(f'The double of \033[34m{number}\033[m is \033[32m{number * 2}\033[m')
print(f'The triple of \033[34m{number}\033[m is \033[32m{number * 3}\033[m')
print(f'The square root of \033[34m{number}\033[m is \033[32m{number  ** (1/2):.2f}\033[m')  # Square root could also be calculated with pow(number, 1/2)
