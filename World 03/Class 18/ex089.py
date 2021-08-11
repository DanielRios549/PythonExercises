'''
    Get the name and two grades of various students and put them in a list.
    In the end, show a bulletin with the media, and allow the user to show the grades of
    each student individually.
'''

students = list()

while True:
    name = input('Name: ')
    grade = [float(input('Grade 1: ')), float(input('Grade 2: '))]
    again = input('Do you want to continue? [Y/N] ')

    students.append([name, grade])

    if again in 'nN':
        break

width = (5, 10, 7)
division = '-' * sum(width)

print(f'{"Nº.":<{width[0]}}{"Name":<{width[1]}}{"Average":<{width[2]}}')
print(division)

for number, student in enumerate(students):
    print(f'{number + 1:<{width[0]}}{student[0]:<{width[1]}}{(student[1][0] + student[1][1]) / 2:>{width[2]}.2f}')

print(division)

while True:
    show = int(input('Do you want to show the grades of which student? [999 to stop]: '))

    if show == 999:
        break

    get = students[show - 1]
    print(f'\033[34m{get[0].title()}\033[m have \033[32m{get[1][0]}\033[m and \033[32m{get[1][1]}\033[m.')
