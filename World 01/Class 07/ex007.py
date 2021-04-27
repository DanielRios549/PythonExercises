'''
    Create a program that reads two grades of a student and calculate its average
'''
grade1 = float(input('What was the first grade? '))
grade2 = float(input('Whats was the second grade? '))

print(f'The average of {grade1:.1f} and {grade2:.1f} is {(grade1 + grade2) / 2:.1f}')
