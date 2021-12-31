from io import TextIOWrapper, UnsupportedOperation
from os import path
import utils.colors as color
import utils.show as show


FILE_DIR = path.join(path.dirname(__file__), 'people')
FILE_NAME = '_people'
FILE_EXT = 'txt'


def exists(filedir: str = FILE_DIR, filename: str = FILE_NAME, ext: str = FILE_EXT):
    exists = False

    try:
        file = open(f'{filedir}/{filename}.{ext}', 'rt')
        file.close()
    except FileNotFoundError:
        exists = False
    else:
        exists = True

    return exists


def create(filedir: str = FILE_DIR, filename: str = FILE_NAME, ext: str = FILE_EXT):
    created = False

    try:
        file = open(f'{filedir}/{filename}.{ext}', 'wt+')

    except UnsupportedOperation:
        print(color.red('There was an error to create the file.'))
        created = False

    else:
        if type(file) == TextIOWrapper:
            created = True
        else:
            created = False

    return created


def read(filedir: str = FILE_DIR, filename: str = FILE_NAME, ext: str = FILE_EXT):
    try:
        file = open(rf'{filedir}/{filename}.{ext}', 'rt')
        lines = file.readlines()
        file.close()

    except FileNotFoundError:
        print(color.red('File does not exists'), color.blue('Try Register someone first.'))

    else:
        for line in lines:
            person = line.replace("\n", "")
            splitted = person.split(',')
            name = splitted[0]
            age = splitted[1]

            rightWidth = 2

            print(f'{name:_<{show.WIDTH - rightWidth}}{age:>{rightWidth}}')


def write(text: str, filedir: str = FILE_DIR, filename: str = FILE_NAME, ext: str = FILE_EXT):
    if exists() is not True:
        create()

    try:
        file = open(f'{filedir}/{filename}.{ext}', 'at')
        file.write(f'\n{text}')
        file.close()

    except UnsupportedOperation:
        print(color.red('Error to add the person.'))

    else:
        print(color.green('Added'))
