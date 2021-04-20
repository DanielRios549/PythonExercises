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
In uppercase it is {name.upper()}.
In lowercase it is {name.lower()}.
It contains {len(''.join(splitted))} letters''')  # The same as len(name) - name.count(' ')

print(f'Your first name is {splitted[0]} and it contains {len(splitted[0])} letters')  # The last is the same as name.find(' ')
