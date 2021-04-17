'''
    Now the teacher want to choose an order for the students presentate the homework. Help him again,
    choosing the order of presentation.
'''
from random import shuffle

student1 = input('Who is the first student? ')
student2 = input('Who is the second? ')
student3 = input('Who is the third? ')
student4 = input('And who is the fourth? ')
students = [student1, student2, student3, student4]
shuffle(students)

print(f'The order of presentation is {students}')
