'''
    Get an angle and show its sine, cosine and tangent
'''
from math import sin, cos, tan, radians

angle = float(input('Whats is the angle? '))

print(f'For an angle of \033[32m{angle}º\033[m')
print(f'The sine is \033[34m{sin(radians(angle)):.2f}\033[m')
print(f'The cosine is \033[35m{cos(radians(angle)):.2f}\033[m')
print(f'And the tangent is \033[36m{tan(radians(angle)):.2f}\033[m')
