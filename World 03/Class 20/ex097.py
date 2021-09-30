'''
    Create a function that prints a text with dynamic width.
'''


def write(text):
    line = '~'
    width = len(text) + 4
    print(line * width)
    print(f'{text:^{width}}')
    print(line * width)


write('Gustavo Guanabara')
write('Curso de Python no YouTube')
write('CeV')
