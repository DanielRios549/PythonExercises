'''
    Get the name of a person and show the first and the last name separately
'''
name = input('What is your name? ').strip().title()
splitted = name.split()

print(f'Nice to meet you, \033[32m{name}!\033[m')
print(f'Your first name is \033[33m{splitted[0]}\033[m')  # Could also be name[:name.find(" ")], without split
print(f'Your last name is \033[35m{splitted[len(splitted) - 1]}\033[m')  # Could also be name[name.rfind(" ") + 1:], without split
