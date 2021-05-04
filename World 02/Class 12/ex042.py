'''
    Remake the exercise 035, adding the feature to show the type of triangle will be created.

    Equilateral: All three sides the same.
    Isosceles: Only two sides the same.
    Scalene: All three sides different.
'''
first = float(input('First line: '))
second = float(input('Second line: '))
third = float(input('Third line: '))

# Verify is the lines can make a triangle

if first + second > third and first + third > second and third + second > first:
    verb = '\033[32mcan\033[m'

    # Identify the type of triangle

    if first == second == third:
        triangle = ' Equilateral'
    elif first != second != third != first:
        triangle = ' Scalene'
    else:
        triangle = ' Isosceles'
else:
    verb = '\033[31mcannot\033[m'
    triangle = ''

print(f'The lines {verb} make a\033[36m{triangle}\033[m triangle.')
