'''
    Create a program that show a person wage and show its new wage with 15% raise
'''
salary = float(input('What\'s the employee salary? R$'))
percent = 15
print(f'A employee that earns R${salary:.2f} will earn R${salary + (salary * percent / 100):.2f} with {percent}% raise')
