'''
    Create a tuple with all teams of the Brazilian Championship, in classification order.
    After the show the following:

    1 - The first 5 teams.
    2 - The last 4 teams.
    3 - A list with the teams in alphabetical order.
    4 - In which position is the Chapecoense team.
'''

table = (
    'RB Bragantino', 'Athletico-PR', 'Palmeiras', 'Fortaleza', 'Bahia', 'Santos', 'Atlético-GO', 'Atlético-MG',
    'Fluminense', 'Flamengo', 'Corinthians', 'Ceara', 'Internacional', 'Juventude', 'Sport Recife', 'Cuiaba',
    'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio'
)
print(f'The teams are: \033[32m{table}\033[m')
questions = ('first', 'last', 'alphabetical', 'position')

for question in questions:
    if question == 'first':
        print(f'The first 5 teams are: \033[34m{table[:6]}\033[m')

    elif question == 'last':
        print('The last 4 teams are: ')

        for team in range(-4, 0, 1):
            print(f'\033[34m{table[team]}\033[m')

    elif question == 'alphabetical':
        print(f'The table in alphabetical order is \033[32m{sorted(table)}\033[m')

    elif question == 'position':
        print(f'\033[34mChapecoense\033[m is in position \033[32m{table.index("Chapecoense") + 1}\033[m')
