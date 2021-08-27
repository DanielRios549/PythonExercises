'''
    Get the name, year of birth, and if they work or not. Put the data in a dict.
    If they work, the dict also will contain the year of the contract and the salary.
    Show the year of vocation too if they work.
'''

from datetime import date

name = input('Name: ').strip().title()
birth = int(input('Year of Birth: '))
work = input('They work? [S/N]').strip()[0]
retireTime = 35
today = date.today().year

employee = {
    'name': name,
    'age': today - birth
}

if work in 'Ss':
    employee['info'] = '\033[32m'
    employee['work'] = True
    employee['contract'] = int(input('Year of the first contract: '))
    employee['salary'] = float(input('What is the salary: R$ '))
    employee['retire'] = employee['age'] + retireTime
else:
    employee['info'] = '\033[31mdo not '
    employee['work'] = False

print('*' * 30)
print(f'''The \033[34mname\033[m is \033[32m{employee["name"]}\033[m.
The \033[34mage\033[m is \033[32m{employee["age"]}\033[m years old.
They {employee["info"]}work\033[m!''')

if employee['work'] is True:
    print(f'The first contract was in \033[32m{employee["contract"]}\033[m')
    print(f'The salary is \033[32mR${employee["salary"]}\033[m')
    print(f'And they will retire with \033[32m{employee["retire"]}\033[m years old in \033[32m{today + retireTime}\033[m')
