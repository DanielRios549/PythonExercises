'''
    Show all the even number between 1 and 50
'''
for count in range(2, 51, 2):
    if count % 10 != 0:
        print(f'\033[34m{count:>2}\033[m', end=' - ')
    else:
        print(f'\033[34m{count}\033[m')
