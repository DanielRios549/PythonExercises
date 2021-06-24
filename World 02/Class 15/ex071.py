'''
    Simulate the operation of a cash machine. First ask the use how many they want to withdraw (integer number).
    The program will inform how many bills of each value will the delievered.

    OBS: The ATM have bills of R$ 50, R$ 20, R$ 10, and R$ 1.
'''

dlength = 20
division = '=-' * dlength
print(f'{division}\n{"Daniel Bank":^{dlength * 2}}\n{division}')

widthdraw = int(input('How many do you want to withdraw? R$ '))
bills50 = bills20 = bills10 = bills1 = 0
toCount = widthdraw
count = 0

while count < widthdraw:
    while toCount >= 50:
        bills50 += 1
        count += 50
        toCount = widthdraw - count
    else:
        print(f'Bills of R$ 50: {bills50}')

    while toCount >= 20:
        bills20 += 1
        count += 20
        toCount = widthdraw - count
    else:
        print(f'Bills of R$ 20: {bills20}')

    while toCount >= 10:
        bills10 += 1
        count += 10
        toCount = widthdraw - count
    else:
        print(f'Bills of R$ 10: {bills10}')

    while toCount >= 1:
        bills1 += 1
        count += 1
        toCount = widthdraw - count
    else:
        print(f'Bills of R$ 1: {bills1}')
