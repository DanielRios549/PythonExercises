'''
    Get the weight of 5 people and show the lowest and the highest ones
'''

weights = []

for count in range(0, 5, 1):
    weights += [float(input(f'What is the {count + 1}º weight? (In KG) '))]

weights.sort()
print(f'The lowest weight is \033[31m{weights[0]:.1f} KG\033[m, and the highest is \033[32m{weights[len(weights) - 1]:.1f} KG\033[m')
