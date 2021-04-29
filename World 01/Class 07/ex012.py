'''
    Create a program that reads the price of a product and show the new price 5% off
'''

price = float(input('What\'s the price of the product? R$'))
print(f'The product costs R$\033[32m{price:.2f}\033[m, the new price is R$\033[32m{price - (price * 5 / 100):.2f}\033[m')
