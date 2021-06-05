'''
    Remake the Exercise 061, adding the feature to the user show more terms.
    Stop when they do not want to show more terms.
'''

first = int(input('What\'s the first term? '))
reason = int(input('What\'s the reason? '))
last = first + (reason * 9)
current = first

while current <= last:
    if current != last:
        print(f'\033[34m{current}\033[m', end=' -> ')
    else:
        print(f'\033[34m{current}\033[m')
        more = input('Show more? [S/N]').strip().upper()

        if more == 'S':
            last = current + (reason * 10)
    current += reason
