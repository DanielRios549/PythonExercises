'''
    Create a function called area() that gets the dimensions of a ground
    and show its area
'''


def area(width, length):
    area = width * length
    print(f'A land with \033[34m{width:.2f}\033[m x \033[34m{length:.2f}\033[m has an area of \033[32m{area:.2f}\033[mm²')


divisor = 20
print('-' * divisor)
print('  Land Dimensions')
print('-' * divisor)

land = (
    float(input('Width (m): ')),
    float(input('Length (m): '))
)

area(land[0], land[1])
