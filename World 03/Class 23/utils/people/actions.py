from time import sleep
import utils.show as show
import utils.file as file
import utils.colors as color


def list():
    info = 'People Registered'
    fileExists = file.exists()

    if fileExists is True:
        show.header(info, len(info) + 4)

    file.read()
    sleep(2)


def register():
    print(color.green('Register will be added soon.'))
    sleep(2)
