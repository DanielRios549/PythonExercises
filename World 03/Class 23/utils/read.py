def readInt(text: str):
    typeText = 'Integer'
    valid = False
    option = 0

    while valid is not True:
        try:
            number = int(input(text).strip())

        except (TypeError, ValueError):
            print(f'\033[31mChoose a valid {typeText} number, please.\033[m')

        except KeyboardInterrupt:
            print('\n\033[34mThe user decides to end the session.\033[m')
            valid = True

        else:
            valid = True
            option = number

    return option


def readFloat(text: str):
    typeText = 'Real'
    valid = False
    option = 0.0

    while valid is not True:
        try:
            number = float(input(text).strip())

        except (TypeError, ValueError):
            print(f'\033[31mChoose a valid {typeText} number, please.\033[m')

        except KeyboardInterrupt:
            print('\n\033[34mThe user decides to end the session.\033[m')
            valid = True

        else:
            valid = True
            option = number

    return option
