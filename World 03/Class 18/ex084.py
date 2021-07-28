'''
    Get the name and the weight of a undefined number of people and put them in a list.
    In the end, show the following:

    1 - How many people were registered.
    2 - The people more heavy.
    3 - The people more light.
'''
people = list()

while True:
    people.append([
        input('Name: '),
        float(input('Weight: (Kg) '))
    ])

    again = input('Do you want to continue? [S/N]: ').strip()

    if again in 'nN':
        break

minPeople = list()
maxPeople = list()
min = max = 0

for index, person in enumerate(people):
    if index < 1:
        min = person[1]
        max = person[1]
    elif person[1] < min:
        min = person[1]
    elif person[1] > max:
        max = person[1]

for person in people:
    if person[1] == min:
        minPeople.append(person[0])
    elif person[1] == max:
        maxPeople.append(person[0])

print(f'You have registered \033[34m{len(people)}\033[m people.')
print(f'The lowest weight is \033[31m{min} Kg\033[m. The weight of {minPeople}')
print(f'Thew highest weight is \033[32m{max} Kg\033[m. The weight of {maxPeople}')
