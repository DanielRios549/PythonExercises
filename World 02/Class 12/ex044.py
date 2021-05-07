'''
    Calculate the price of a product according to the pay method.

    In cash: 10% off
    Once with credit card: 5% off
    Twice with credit card: default price
    More than 3 times no cartão: 20% fee
'''

print(f'{" Daniel Store ":=^40}')

price = float(input('How much the product costs? R$'))
method = int(input('''

How do you want to pay

[ 1 ] In cash
[ 2 ] Once with credit card
[ 3 ] Twice with credit card
[ 4 ] More than three times

'''))
options = [1, 2, 3, 4]

if method in options:
    if method == 1:
        newPrice = price - (price * 10 / 100)
    elif method == 2:
        newPrice = price - (price * 5 / 100)
    elif method == 3:
        newPrice = price
        print(f'The price will be divided \033[34mwithout fee\033[m, the installment will be \033[34mR$ {newPrice / 2:.2f}\033[m per month for 2 months long.')
    else:
        newPrice = price + (price * 20 / 100)
        installment = int(input('What will be the installment? '))
        print(f'The price will be divided \033[31mwith fee\033[m, the installment will be \033[34mR${newPrice / installment:.2f}\033[m per month for {installment} months long.')

    print(f'The product that costs \033[34mR${price:.2f}\033[m will cost \033[34mR${newPrice:.2f}\033[m with this payment method.')
else:
    print('Enter a valid option, please')
