'''
    Create a program that reads the height and width of a wall, calculate its area and the paint necessary to paint it,
    knowing that each liter of paint paints 2m²
'''
width = float(input('What\'s the width of the wall? '))
height = float(input('What\'s the height of the wall? '))
area = width * height

print(f'Your wall has {width:.2f}x{height:.2f} m and has a area of {area:.2f} m².')
print(f'To paint it, you\'ll need {area / 2} liters of paint.')  # Could also be area * 0.5 or area * (1/2)
