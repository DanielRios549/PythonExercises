'''
    The National swimming organization needs to get the year of birth
    of its athletes to show its category.

    Until 9 years old: Little
    Until 14 years old: Infantile
    Until 19 years old: Junior
    Until 25 years old: Senior
    More than 20 years old: Master
'''
from datetime import date

year = int(input('When the athlete born? '))
age = date.today().year - year

if age <= 9:
    category = 'Little'
elif age <= 14:
    category = 'Infantile'
elif age <= 19:
    category = 'Junior'
elif age <= 25:
    category = 'Senior'
else:
    category = 'Master'

print(f'An athlete with \033[34m{age}\033[m years old is \033[34m{category}\033[m')
