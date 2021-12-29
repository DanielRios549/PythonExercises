'''
    This script facilities the addition of scaped ANSI colors in strings.
'''

end = '\033[m'


def red(text):
    return f'\033[31m{str(text)}{end}'


def green(text):
    return f'\033[32m{str(text)}{end}'


def yellow(text):
    return f'\033[33m{str(text)}{end}'


def blue(text):
    return f'\033[34m{str(text)}{end}'


def purple(text):
    return f'\033[35m{str(text)}{end}'


def light_blue(text):
    return f'\033[36m{str(text)}{end}'


def gray(text):
    return f'\033[37m{str(text)}{end}'
