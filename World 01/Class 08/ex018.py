'''
    Get an angle and show its sine, cosine and tangent
'''
from math import sin, cos, tan, radians

angle = float(input('Whats is the angle? '))

print(f'For an angle of {angle}º')
print(f'The sine is {sin(radians(angle)):.2f}')
print(f'The cosine is {cos(radians(angle)):.2f}')
print(f'And the tangent is {tan(radians(angle)):.2f}')
