'''
    Show the follwing information of the name of a person:

    1 - The same name with all the words in upper case
    2 - The same name with all the words in lower case
    3 - How many words it contains, without the spaces
    4 - How many words contain the first name
'''
name = input('Type your complete name: ').strip()
splitted = name.split()

print(f''' Analysing your name...
In uppercase it is \033[32m{name.upper()}\033[m.
In lowercase it is \033[34m{name.lower()}.\033[m
It contains \033[33m{len(''.join(splitted))}\033[m letters''')  # The same as len(name) - name.count(' ')

print(f'Your first name is \033[35m{splitted[0]}\033[m and it contains \033[36m{len(splitted[0])}\033[m letters')  # The last is the same as name.find(' ')
