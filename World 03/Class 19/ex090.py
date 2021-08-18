'''
    Get the name and average of a student fro the user, and add the situation.
    In the end, show the content of the structure.
'''

student = dict()

name = input('Name: ')
average = float(input(f'Average of {name}: '))

student['name'] = name
student['average'] = average

if average < 5:
    student['status'] = '\033[31mReproved\033[m'
elif average < 6:
    student['status'] = '\033[33mRetaken\033[m'
else:
    student['status'] = '\033[32mApproved\033[m'

print(f'''{"-=" * 20}
    - The name is {student["name"]}
    - The average is {student["average"]}
    - The situation is {student["status"]}
''')
