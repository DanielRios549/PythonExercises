'''
    Get the name of a person and show the first and the last name separately
'''
name = input('What is your name? ').strip().title()
splitted = name.split()

print(f'Nice to meet you, {name}!')
print(f'Your first name is {splitted[0]}')  # Could also be name[:name.find(" ")], without split
print(f'Your last name is {splitted[len(splitted) - 1]}')  # Could also be name[name.rfind(" ") + 1:], without split
