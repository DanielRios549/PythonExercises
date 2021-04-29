'''
    Create a program that reads the height and width of a wall, calculate its area and the paint necessary to paint it,
    knowing that each liter of paint paints 2m²
'''
width = float(input('What\'s the width of the wall? '))
height = float(input('What\'s the height of the wall? '))
area = width * height

print(f'Your wall has \033[34m{width:.2f}\033[mx\033[34m{height:.2f}\033[m m and has a area of \033[32m{area:.2f}\033[m m².')
print(f'To paint it, you\'ll need \033[36m{area / 2:.2f}\033[m liters of paint.')  # Could also be area * 0.5 or area * (1/2)
