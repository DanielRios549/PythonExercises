'''
    Remake the exercise 064, now using break.
'''

number = result = count = 0

while True:
    number = int(input('type a number: [999 to stop] '))

    if number == 999:
        break

    result += number
    count += 1

print(f'You chose \033[34m{count}\033[m numbers and the sum of them equals \033[34m{result}\033[m.')
