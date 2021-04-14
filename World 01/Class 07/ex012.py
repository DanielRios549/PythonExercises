'''
    Create a program that reads the price of a product and show the new price 5% off
'''

price = float(input('What\'s the price of the product? R$'))
print(f'The product costs R${price:.2f}, the new price is R${price - (price * 5 / 100):.2f}')
