'''
    Get an year and shows if it is a leap year.
'''
from datetime import date

question = int(input('What year do you want to analyse? Type 0 to the current one: '))
current = date.today().year

# Define the year

if question == 0:
    year = current
else:
    year = question

# Verify if it is a leap and define the verb for past and future

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:  # Divisible by 4, 100 and 400
            leap = True
            verb = 'was' if year < current else 'will be'
        else:  # Divisible by 4 and 100 but not by 400
            leap = False
            verb = 'wasn\'t' if year < current else 'won\'t'
    else:  # Divisible by 4 but not by 100
        leap = True
        verb = 'was' if year < current else 'will be'
else:  # Not divisible by 4
    leap = False
    verb = 'wasn\'t' if year < current else 'won\'t'

# Define the verb for the current year

if year == current:
    verb = 'is' if leap is True else 'isn\'t'

print(f'{year} {verb} a leap year.')
