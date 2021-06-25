'''
    Get the age a gender of an undefined number of people.
    For each single person, the program should ask if the user wants to continue.
    In the end, show the following:

    1 - How many people are higher than 18 years old.
    2 - How many of them are man.
    3 - How many women are lower than 20 years old.
'''

dlength = 20
division = '-=' * dlength
print(f'{division}\n{"People Register":^{dlength * 2}}\n{division}')

all18 = man = women20 = 0

while True:
    age = int(input('Age: '))
    gender = input('Gender: [M/F]').strip().upper()

    if age > 18:
        all18 += 1

    if gender == 'M':
        man += 1
    elif gender == 'F' and age < 20:
        women20 += 1

    again = input('Do you want to continue? [S/N]').strip().upper()

    if again == 'N':
        break

print(f'People higher than \033[34m18\033[m years old: \033[32m{all18}\033[m')
print(f'We have \033[32m{man}\033[m men at all, and \033[32m{women20}\033[m women lower than \033[34m20\033[m years old.')
