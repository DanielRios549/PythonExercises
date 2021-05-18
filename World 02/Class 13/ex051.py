'''
    Get the first term and the reason of an Arithmetic Progression.
    Show all the 10 firsts ones.
'''

first = int(input('What is the firm term? '))
reason = int(input('And what is the reason? '))
last = first + (reason * 10)

print(f'The 10 firsts items of an Arithmetic Progression starting in \033[32m{first}\033[m, with a reason of \033[32m{reason}\033[m is: ')

for count in range(first, last, reason):
    if count != last - reason:
        print(f'\033[34m{count}\033[m', end=' -> ')
    else:
        print(f'\033[34m{count}\033[m')
