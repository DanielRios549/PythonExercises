'''
    Create a script that reads something and show the type and all informations about it.
'''
something = input('Type something: ')

print(f'The type of this value is {type(something)}')
print(f'Has only spaces? {something.isspace()}')
print(f'Is numeric? {something.isnumeric()}')
print(f'Is alphabetic? {something.isalpha()}')
print(f'Is alphamumeric? {something.isalnum()}')
print(f'Is uppercase? {something.isupper()}')
print(f'Is lowercase? {something.islower()}')
print(f'Is capital? {something.istitle()}')
print(f'Is decimal? {something.isdecimal()}')
print(f'Is digit? {something.isdigit()}')
print(f'Is printable? {something.isprintable()}')
print(f'Is identifier? {something.isidentifier()}')
