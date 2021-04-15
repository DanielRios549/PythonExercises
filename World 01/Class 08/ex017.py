'''
    Get the lengh of the adjacent and the opposite side of a rectangle triangle, and show its hypotenuse
'''
from math import hypot

opposite = float(input('What\'s the lengh of the opposite side? '))
adjacent = float(input('What\'s the lengh of the adjacent side? '))

print(f'The hypotenuse is {hypot(opposite, adjacent):.2f}')  # Hypotenuse could be calcutated with (opposite ** 2 + adjacent ** 2) ** 0.5
