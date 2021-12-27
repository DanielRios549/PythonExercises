def format(number: float):
    return f'R${number:.2f}'.replace('.', ',')


def inputCoin(text: str):
    number = input(text).strip()
    numberFix = number.replace(",", ".")
    check = number.replace(',', '').replace('.', '')

    if check.isnumeric():
        return float(numberFix)
    else:
        print(f'Error: \033[31m"{numberFix}"\033[m is not a valid price.')
