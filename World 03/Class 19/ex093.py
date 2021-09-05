'''
    Manage the performance of a football player. Get the name and the number of maches.
    For each match, get the numbers of goals the player scores.
    In the end, put all the data in a dict, including the total of goals scored by the player.
'''

division = '*='
count = 30
divisor = division * count

player = {
    'name': input('Player Name: ').strip().title(),
    'matches': int(input('Matches played: ')),
    'goals': list(),
    'total': 0
}

for match in range(0, player['matches']):
    goals = int(input(f'\tGoals in the \033[32m{match + 1}º\033[m match? '))
    player['goals'].append(goals)

    player['total'] += goals

player.__delitem__('matches')

print(divisor)

print(player)

print(divisor)

for key, value in player.items():
    print(f'The key \033[32m{key}\033[m has value of \033[34m{value}\033[m')

print(divisor)

print(f"The player called \033[32m{player['name']}\033[m plays \033[34m{len(player['goals'])}\033[m matches.")

for index, value in enumerate(player['goals']):
    print(f'\t=> In the \033[32m{index + 1}º\033[m match, \033[34m{value}\033[m goals.')

print(f"A total of \033[32m{player['total']}\033[m goals.")
