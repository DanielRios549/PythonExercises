from time import sleep
import utils.show as show
import utils.file as file


def list():
    info = 'People Registered'
    fileExists = file.exists()

    if fileExists is True:
        show.header(info)

    file.read()
    sleep(2)


def register(name: str, age: int):
    file.write(f'{name},{age}')
    sleep(2)
