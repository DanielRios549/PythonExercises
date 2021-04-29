'''
    Create a script that reads something and show the type and all informations about it.
'''
something = input('Type something: ')

print(f'The type of this value is \033[34m{type(something)}\033[m')
print(f'Has only spaces? \033[34m{something.isspace()}\033[m')
print(f'Is numeric? \033[34m{something.isnumeric()}\033[m')
print(f'Is alphabetic? \033[34m{something.isalpha()}\033[m')
print(f'Is alphamumeric? \033[34m{something.isalnum()}\033[m')
print(f'Is uppercase? \033[34m{something.isupper()}\033[m')
print(f'Is lowercase? \033[34m{something.islower()}\033[m')
print(f'Is capital? \033[34m{something.istitle()}\033[m')
print(f'Is decimal? \033[34m{something.isdecimal()}\033[m')
print(f'Is digit? \033[34m{something.isdigit()}\033[m')
print(f'Is printable? \033[34m{something.isprintable()}\033[m')
print(f'Is identifier? \033[34m{something.isidentifier()}\033[m')
