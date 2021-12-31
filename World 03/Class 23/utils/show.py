import utils.colors as color

WIDTH = 40


def line(width: int = WIDTH + 4):
    separator = '-'
    print(color.blue(separator * width))


def header(text: str = 'Header', width: int = WIDTH):
    line(width)
    print(color.green(text.center(width)))
    line(width)
