'''
    Get the weight of 5 people and show the lowest and the highest ones
'''

weights = []

for count in range(0, 5, 1):
    weights += [float(input(f'What is the {count + 1}º weight? Kg '))]

weights.sort()
print(f'The lowest weight is Kg {weights[0]:.1f} and the highest is Kg {weights[len(weights) - 1]:.1f}')
print(weights)
