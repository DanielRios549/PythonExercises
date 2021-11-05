'''
    Create a function called 'stats' that takes two optional parameters.
    The name of the player and the numbers of goals scored.

    You should return the player data even if some information was not provided.
'''

while True:
    default = ('<Unknown>', '0')

    def stats(player: str = default[0], goals: str = default[1]):
        if len(player) == 0:
            player = default[0]
        if len(goals) == 0 or not goals.isnumeric():
            goals = default[1]

        return f'The player \033[32m{player}\033[m scores \033[34m{goals}\033[m goal(s) in the championship'

    print(stats(
        input('Player Name: ').strip(),
        input('Goals: ').strip()
    ))

    again = input('Againg? [Y/N]').upper()

    if again[0:1] in 'nN':
        break
