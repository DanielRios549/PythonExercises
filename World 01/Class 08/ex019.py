'''
    A teacher wants to choose one of its students to erase the board. Help him,
    getting the names of all students and choosing one of them
'''
from random import choice

student1 = input('Who is the first student? ')
student2 = input('Who is the second? ')
student3 = input('Who is the third? ')
student4 = input('And who is the fourth? ')
students = [student1, student2, student3, student4]

print(f'The chosen student is {choice(students)}')
