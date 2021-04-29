'''
    Create a program that reads a value in meters and show it converted
'''
meters = float(input('What is the measure? '))

print(f'\033[35m{meters}\033[m meters is the same as')
print(f'\033[31m{meters / 1000:.3f}\033[m km')
print(f'\033[32m{meters / 100:.2f}\033[m hm')
print(f'\033[33m{meters / 10:.1f}\033[m dam')
print(f'\033[34m{meters * 10:.0f}\033[m dm')
print(f'\033[35m{meters * 100:.0f}\033[m cm')
print(f'\033[36m{meters * 1000:.0f}\033[m mm')
