'''
    Create a program that show a person wage and show its new wage with 15% raise
'''
salary = float(input('What\'s the employee salary? R$'))
percent = 15
print(f'An employee that earns R$\033[34m{salary:.2f}\033[m will earn R$\033[32m{salary + (salary * percent / 100):.2f}\033[m with \033[36m{percent}\033[m% raise')
