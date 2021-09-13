'''
    Get the name, gender and age of a undefined number of people, and put the each data in a dict,
    and all the dicts in a list.

    In the end, show the following:

    1 - How many people were registered.
    2 - The average age.
    3 - A list of all women.
    4 - A list with all people with age higher than the average.
'''

people = list()
stop = False

while stop is False:
    data = {
        'name': input('Name: ').strip().title(),
        'gender': input('Gender [M/F]: ').strip().upper(),
        'age': int(input('Age: '))
    }
    people.append(data)
    again = '?'

    while again not in 'YN':
        again = input('Continue? [Y/N]: ').strip().upper()

        if again not in 'YN':
            print('please, use only \033[34mY\033[m or \033[34mN\033[m')

        if again == 'N':
            stop = True

# The method used to sum the ages is called comprehension

average = (sum(person["age"] for person in people)) / len(people)

women = list()
higher = list()

for person in people:
    if person["gender"] == 'F':
        women.append(person["name"])

    if person["age"] > average:
        higher.append(person['name'])

print('*' * 30)

print(f'1 - We have \033[34m{len(people)}\033[m people registered.')
print(f'2 - The average age is \033[34m{average:.2f}\033[m years old.')
print(f'3 - The women registered are \033[34m{women if len(women) >= 1 else "Nobody"}\033[m.')
print(f'4 - The people higher than the average are \033[34m{higher if len(higher) >= 1 else "Nobody"}\033[m.')
