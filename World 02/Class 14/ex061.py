'''
    Remake the Exercise 051, now using while instead of for.

    It consists in getting the first item and the reason of a Arithmetic Progression.
    Show only the firsts ten items.
'''

first = int(input('What\'s the number? '))
reason = int(input('What\'s the term? '))
last = first + (reason * 9)
current = first

while current <= last:
    if current != last:
        print(f'\033[34m{current}\033[m -> ', end='')
    else:
        print(f'\033[34m{current}\033[m')
    current += reason
