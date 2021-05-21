'''
    Get the date of birth of 7 people, and show how many is not adult
    and how many is.
'''
from datetime import date

people = [0, 0]
today = date.today().year

for count in range(0, 7):
    person = int(input('When the person born? '))

    if today - person > 18:
        people[0] += 1
    else:
        people[1] += 1

print(f'{people[0]} are adults and {people[1]} are not')
