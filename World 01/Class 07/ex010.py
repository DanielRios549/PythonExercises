'''
    Create a program that show how money a person has in the wallet, and show how many dollars they can buy,
    considering 1 dollar equals R$ 5.73
'''
money = float(input('How money do you have in the wallet? R$ '))
print(f'With R$ \033[32m{money:.2f}\033[m you can by US$ \033[34m{money / 5.73:.2f}\033[m and €$ \033[34m{money / 6.68:.2f}\033[m')
