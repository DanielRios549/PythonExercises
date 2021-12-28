def readNumber(text: str, readType: str = 'float'):
    convert = str
    typeText = ''

    if readType == 'int':
        convert = int
        typeText = 'Integer'
    elif readType == 'float':
        convert = float
        typeText = 'Real'

    readTypes = ('int', 'float')

    if readType in readTypes:
        number = None
        valid = False

        while valid is not True:
            try:
                number = convert(input(text).strip())

            except (TypeError, ValueError):
                print(f'\033[31mChoose a valid {typeText} number, please.\033[m')

            except KeyboardInterrupt:
                print('\n\033[34mThe user decides to end the session.\033[m')
                valid = True

            else:
                valid = True
                return number

    else:
        print('This function works only with \033[34mInteger\033[m and \033[34mReal\033[m numbers.')


def readInt(text: str):
    return readNumber(text, 'int')


def readFloat(text: str):
    return readNumber(text, 'float')
