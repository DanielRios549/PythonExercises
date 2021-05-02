'''
    Get the year of birth and show a message according to its age:

    If him need to enlist himself to the army in the future.
    If it is time for him to enlist now.
    If he is late, he should enlisted in the past.
'''
from datetime import date

year = int(input('What year do you born? '))
today = date.today().year
enlistment = year + 18


if enlistment == today:
    verb = '\033[32mis happen now\033[m!'
    complement = 'enlist yourself \033[34mthis year\033[m!'
elif enlistment < today:
    verb = '\033[31malready happen\033[m!'
    complement = f'enlisted yourself in \033[34m{enlistment}\033[m.'
elif enlistment > today:
    verb = '\033[34mis about to happen\033[m.'
    complement = f'enlist yourself in \033[36m{enlistment}\033[m.'

print(f'Who born in \033[35m{year}\033[m has \033[35m{today - year}\033[m years old in \033[35m{today}\033[m')
print(f'Your enlistment {verb}\nYou should {complement}')
