'''
    Get a person's name and show if it contains 'Silva'
'''
name = input('What is you name? ').strip()
print(f'Is it contains Silva? {"silva" in name.lower()}')
