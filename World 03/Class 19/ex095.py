'''
    Remake the Exercise 093, making it work to various players.
    Adding a visualization for the performance of each player.
'''

team = list()
tabulation = '---->  '

while True:
    player = {
        'name': input('Player Name: ').strip().title(),
        'matches': int(input('Matches played: ')),
        'goals': list(),
        'total': 0
    }

    for match in range(0, player['matches']):
        goals = int(input(f'{tabulation}Goals in the \033[32m{match + 1}º\033[m match? '))
        player['goals'].append(goals)

        player['total'] += goals

    player.__delitem__('matches')
    team.append(player)

    while True:
        again = input('Do you want to continue? [Y/N] ').strip().upper()[0]

        if again not in 'YN':
            print('Choose only \033[34mY\033[m (yes) or \033[34mN\033[m (no), please.')
        else:
            break

    if again == 'N':
        break


division = '*='
table = (3, 20, 20, 6)
line = "-" * (sum(table) + 2)

# Print the lines according to the width of the table

count = (sum(table) // len(division)) + 1
divisor = division * count

print(divisor)

print(f'{"Nº":>{table[0]}}  {"Name":<{table[1]}}{"Goals":<{table[2]}}{"Total":<{table[3]}}')
print(line)

for index, player in enumerate(team):
    goals = ""

    for match, goal in enumerate(player["goals"]):
        end = ', '

        if match + 1 == len(player["goals"]):
            end = ''

        goals += f'{goal}{end}'

    print(f'{index + 1:>{table[0]}}  {player["name"]:<{table[1]}}{goals:<{table[2]}}{player["total"]:<{table[3]}}')

print(line)
print(divisor)

while True:
    while True:
        show = int(input('Show information for which player? [999 to stop]: '))

        if show != 999:
            if show > len(team):
                print(line)
                print('This player \033[31mdoes not exist\033[m. Choose another from table above.')
                print(line)
            else:
                player = team[show - 1]
                print(line)
                print(f'The player {player["name"]} has the following stats:')
                print(line)

                for index, goal in enumerate(player['goals']):
                    print(f'{tabulation}Match \033[34m{index + 1}\033[m: Scores \033[32m{goal}\033[m goals.')
        else:
            break

    if show == 999:
        break
