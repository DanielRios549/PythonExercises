'''
    Create a program that show how money a person has in the wallet, and show how many dollars they can buy,
    considering 1 dolar equals R$ 5.73
'''
money = float(input('How money do you have in the wallet? R$ '))
print(f'With R$ {money:.2f} you can by US$ {money / 5.73:.2f} and €$ {money / 6.68:.2f}')
