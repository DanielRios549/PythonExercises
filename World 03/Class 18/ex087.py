'''
    Remake the previous exercise, showing in the end:

    1 - The sum of all even numbers.
    2 - The sum of all number in the last column.
    3 - The highest number of the second line.
'''

matrix = []
column = line = 0
lines = int(input('Numbers of lines: '))
columns = int(input('Numbers of Columns: '))
even = last = 0

division = '=*'
width = 30
text = f'Creating a {lines} x {columns} Matrix'
print(f'{division * width}\n{text:^{width * 2}}\n{division * width}')

for count in range(0, lines):
    matrix.append(list())

for count in range(0, lines * columns):
    if column == columns:
        line += 1
        column = 0

    matrix[line].append(int(input(f'Choose a number for {line + 1, column + 1}: ')))
    column += 1

print(division * width)

for line in matrix:
    for item in line:
        print(f'[{item:^5}]', end='')

        if item % 2 == 0:
            even += item
        if item == line[-1]:
            last += item
    print()

print(division * width)

print(f'The sum of all \033[32meven number\033[m equals \033[34m{even}\033[m')
print(f'The sum of all item of the \033[32mlast column\033[m equals \033[34m{last}\033[m')
print(f'The highest item of the \033[32msecond line\033[m is \033[34m{max(matrix[1])}\033[m')
