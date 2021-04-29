'''
    Create a program that reads two grades of a student and calculate its average
'''
grade1 = float(input('What was the first grade? '))
grade2 = float(input('Whats was the second grade? '))

print(f'The average of \033[34m{grade1:.1f}\033[m and \033[34m{grade2:.1f}\033[m is \033[32m{(grade1 + grade2) / 2:.1f}\033[m')
