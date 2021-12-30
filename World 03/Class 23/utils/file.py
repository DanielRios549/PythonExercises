from io import TextIOWrapper, UnsupportedOperation
from os import path
import utils.colors as color

FILE_DIR = path.join(path.dirname(__file__), 'people')
FILE_NAME = '_people'
FILE_EXT = 'txt'


def exists(name: str = FILE_NAME, ext: str = FILE_EXT):
    exists = False

    try:
        open(f'{FILE_DIR}/{name}.{ext}')
    except FileNotFoundError:
        exists = False
    else:
        exists = True

    return exists


def create(name: str = FILE_NAME, ext: str = FILE_EXT):
    created = False

    try:
        file = open(f'{FILE_DIR}/{name}.{ext}', 'wt+')

    except UnsupportedOperation:
        print(color.red('There was an error to create the file.'))
        created = False

    else:
        if type(file) == TextIOWrapper:
            created = True
        else:
            created = False

    return created


def read(name: str = FILE_NAME, ext: str = FILE_EXT):
    try:
        file = open(rf'{FILE_DIR}/{name}.{ext}', 'r+')
        lines = file.readlines()

    except FileNotFoundError:
        print(color.red('File does not exists'), color.blue('Try Register someone first.'))

    else:
        print(lines)
