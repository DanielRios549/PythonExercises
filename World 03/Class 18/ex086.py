'''
    Create a 3x3 matrix and put values on it.
    In the end, show the matrix with the correct format.
'''

matrix = [[], [], []]
line = column = 0

for count in range(0, 9):
    matrix[line].append(int(input(f'Choose a number for [{line}, {column}]: ')))
    column += 1

    if column == 3:
        line += 1
        column = 0

for line in matrix:
    for item in line:
        print(f'[{item:^5}]', end='')
    print()
