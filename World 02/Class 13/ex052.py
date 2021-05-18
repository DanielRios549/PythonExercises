'''
    Get an integer number and show if it is a prime number or not
'''

number = int(input('Choose an integer number: '))

if number < 1:
    print('Choose a natural number, please.')
elif number == 1:  # 1 is not prime
    prime = False
elif number == 2 or number == 3:  # 2 and 3 both are prime
    prime = True
elif number % 2 == 0:  # Even numbers higher than 3 are always not prime
    prime = False
else:
    prime = True  # By default, odd numbers higher than 3 are prime, unless...
    for count in range(3, number // 2, 1):
        if number % count == 0:  # ...Unless it founds a divisible number other than one and itself
            prime = False
            break

    if prime is True:
        print('\033[32mPRIME\033[m')
    else:
        print('\033[31mNot PRIME\033[m')
