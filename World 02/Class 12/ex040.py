'''
    Remake the Exercise 007, showing a mesage according to the avarage

    Less than 5.0 - Reproved
    Between 5.0 and 6.9 - Retaken
    More than 7.0 - Approved
'''

grade1 = float(input('What was the first grade? '))
grade2 = float(input('What was the second grade? '))
average = (grade1 + grade2) / 2

if average < 5.0:
    status = '\033[31mREPROVED\033[m'
elif average > 7:
    status = '\033[32mAPPROVED\033[m'
else:
    status = '\033[33mIN RETAKEN\033[m'

print(f'The average of \033[34m{grade1:.1f}\033[m and \033[34m{grade2:.1f}\033[m is \033[35m{average:.1f}\033[m, you are {status}')
