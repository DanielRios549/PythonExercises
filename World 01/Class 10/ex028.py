'''
    Make the computer choose one number from 0 to 5, and asks the user if they know what was the number.
    The script should print if the user wins of loses.
'''
from random import randint
from time import sleep

number = randint(0, 5)

print('-=-' * 20)
print('I will choose a number from 0 to 5. Guess what?')
print('-=-' * 20)

answer = int(input('What number did I choose? '))
print('PROCESSING...')
sleep(3)

if number == answer:
    print(f'You win! I thought in the number {number}')
else:
    print(f'You loose! I thought in the number {number} and not in the {answer}')
