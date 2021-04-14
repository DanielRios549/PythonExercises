'''
    Create a program that converts a temperature in ºC to ºF
'''

celsius = float(input('Type the temperature in ºC: '))
fahrenheit = ((celsius * 9) / 5) + 32  # Could also be celsius * 9 / 5 + 32, without the parentesis, because of the precedence order
kelvin = celsius + 273.15

print(f'{celsius:.1f}ºC is the same as {fahrenheit:.1f}ºF and {kelvin}K')
