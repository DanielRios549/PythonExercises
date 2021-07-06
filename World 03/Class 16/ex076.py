'''
    Create a unique tuple with product followed by their respective prices.
    In the end, show them organized in a table like this:

    Product......................R$  25.00
    Product2.....................R$ 125.00
    Product3.....................R$   2.00
'''
count = 50
divisor = '-' * count
print(f'{divisor}\n{"Price List":^{count}}\n{divisor}')

products = (
    'Pencil', 1.75,
    'Eraser', 2.00,
    'Notebook', 15.90,
    'Pencil Case', 25.00,
    'Protractor', 4.20,
    'Compass', 9.99,
    'Back Pack', 120.32,
    'Pens', 22.30,
    'Book', 34.90
)

for product in products:
    if type(product) == str:
        print(f'{product:.<{count - 10}}', end='')
    else:
        print(f'R${product:>8.2f}')
