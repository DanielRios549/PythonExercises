'''
    Get the name, age and gender of 4 people, and show the following:

    1 - The average of age.
    2 - The name of the oldest person.
    3 - How many women have less then 20 years old.
'''
ages = []
oldest = ''
w_under = 0

# Get the info of people

for count in range(0, 4, 1):
    person = str(count + 1) + 'º person'
    division = '=+' * 20

    print(division)
    print(f'{person:^40}')
    print(division)

    name = input(f'What\'s the {person} name? ').strip().title()
    age = int(input(f'How is their age? ').strip())
    gender = input(f'And what\'s their gender? (M/F) ').strip().upper()

    ages.append(age)

    if max(ages) == age:
        oldest = name
    if gender == 'F' and age < 20:
        w_under += 1

print(f'The avarage of age is \033[34m{sum(ages) / len(ages):.0f}\033[m years old')
print(f'The name of the oldest person is \033[34m{oldest}\033[m')
print(f'There is \033[34m{w_under}\033[m women the have less then 20 years old.')
