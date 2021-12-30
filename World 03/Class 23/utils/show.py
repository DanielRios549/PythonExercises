import utils.colors as color


def line(width: int = 0):
    separator = '-'
    print(color.blue(separator * width))


def header(text: str = 'Header', width: int = 10):
    line(width)
    print(color.green(text.center(width)))
    line(width)
