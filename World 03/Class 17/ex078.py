'''
    Get 5 values and put them in a list.
    In the end, show the lowest and the highest and their indexes in the list.
'''

values = []

for count in range(0, 5):
    value = int(input(f'Choose a value for the position {count}: '))
    values.append(value)

low = []
high = []

for index, value in enumerate(values):
    if value == min(values):
        low.append(index)
    elif value == max(values):
        high.append(index)

print(f'You choose the values {values}')
print(f'The lowest value is {min(values)} in the positions {low}')
print(f'And the highest is {max(values)} in the positions {high}')
