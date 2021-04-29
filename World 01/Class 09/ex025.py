'''
    Get a person's name and show if it contains 'Silva'
'''
name = input('What is you name? ').strip()
print(f'Is it contains Silva? \033[33m{"silva" in name.lower()}\033[m')
