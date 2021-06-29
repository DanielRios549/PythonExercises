'''
    Create a tuple writing numbers in words from 0 to 20. Ask the user a number from 0 to 20,
    and show the number in words using the item on the tuple.
'''

numbers = (
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
)
number = -1

while number < 0 or number > 20:
    number = int(input('Choose a number from 1 to 20: '))

print(f'The number \033[34m{number}\033[m in words is \033[32m{numbers[number]}\033[m')
