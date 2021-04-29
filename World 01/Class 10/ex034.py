'''
    Asks the wage of an employee and show the percentage of its raise.
    For employees with a wage higher than R$ 1250, the raise will be 10%,
    For employees with a wage lower than that, the raise will be 15%.
'''
salary = float(input('What is the employee salary? R$'))

if salary <= 1250:
    percent = 15
else:
    percent = 10

print(f'An employee that earns \033[34mR${salary:.2f}\033[m will earn \033[32mR${salary + (salary * percent / 100):.2f}\033[m with \033[35m{percent}%\033[m raise.')
