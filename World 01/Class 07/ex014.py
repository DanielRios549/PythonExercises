'''
    Create a program that converts a temperature in ºC to ºF
'''

celsius = float(input('Type the temperature in ºC: '))
fahrenheit = ((celsius * 9) / 5) + 32  # Could also be celsius * 9 / 5 + 32, without the parentheses, because of the precedence order
kelvin = celsius + 273.15

print(f'\033[32m{celsius:.1f}\033[mºC is the same as \033[34m{fahrenheit:.1f}\033[mºF and \033[35m{kelvin}\033[mK')
