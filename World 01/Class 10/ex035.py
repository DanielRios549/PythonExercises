'''
    Asks for three sides of a line, and show it they can create a triangle.
'''
first = float(input('First line: '))
second = float(input('Second line: '))
third = float(input('Third line: '))

if first + second > third and first + third > second and third + second > first:
    verb = '\033[32mcan\033[m'
else:
    verb = '\033[31mcannot\033[m'

print(f'These lines {verb} create a triangle!')
