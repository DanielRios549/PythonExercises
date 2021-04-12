'''
    Create a program that reads a value in meters and show it converted
'''
meters = float(input('What is the measure? '))

print(f'{meters} meters is the same as')
print(f'{meters / 1000:.3f}km')
print(f'{meters / 100:.2f}hm')
print(f'{meters / 10:.1f}dam')
print(f'{meters * 10:.0f}dm')
print(f'{meters * 100:.0f}cm')
print(f'{meters * 1000:.0f}mm')
