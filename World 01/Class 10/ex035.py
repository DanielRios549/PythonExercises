'''
    Asks for three sides of a line, and show it they can create a triangle.
'''
first = float(input('First line: '))
second = float(input('Second line: '))
third = float(input('Third line: '))

if first + second > third and first + third > second and third + second > first:
    verb = 'can'
else:
    verb = 'cannot'

print(f'These lines {verb} create a triangle!')
