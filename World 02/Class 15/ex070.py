'''
    Get the name and the value of various products.
    The program should ask if the user wants to continue.
    In the end show the following:

    1 - The total value.
    2 - How many products costs more than R$1000.
    3 - The name of cheaper product.
'''

dlength = 20
division = '=-' * dlength
print(f'{division}\n{"The Cheapest Shop":^{dlength * 2}}\n{division}')

total = higher1000 = cheapestValue = cheapestName = 0

while True:
    name = input('Product name: ')
    price = float(input('Price: R$ '))

    if total == 0:
        cheapestValue = price
        cheapestName = name
    elif price < cheapestValue:
        cheapestValue = price
        cheapestName = name

    total += price

    if price > 1000:
        higher1000 += 1

    again = input('Do you want to continue? [S/N]').strip().upper()

    if again == 'N':
        break

print(f'The total cost is \033[32mR$ {total:.2f}\033[m, with \033[32m{higher1000}\033[m products higher than \033[34mR$ 1000\033[m')
print(f'And the cheapest product is the \033[32m{cheapestName}\033[m, it costs R$ {cheapestValue:.2f}\033[m')
