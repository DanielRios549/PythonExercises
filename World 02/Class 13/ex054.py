'''
    Get the date of birth of 7 people, and show how many is not adult
    and how many is.
'''
from datetime import date

people = [0, 0]
today = date.today().year

for count in range(0, 7):
    person = int(input(f'When the {count + 1}º person born? '))

    if today - person > 18:
        people[0] += 1
    else:
        people[1] += 1

print(f'\033[34m{people[0]}\033[m are adults and \033[31m{people[1]}\033[m are not')
