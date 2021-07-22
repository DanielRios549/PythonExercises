'''
    Get an expression that uses parenthesis.
    You have to analyse if the expression have the brackets opened and closed in the correct possition.
    The expression looks like this:
    ((a + b) / c) * d
'''

expression = str(input('Type a Mathematical Expression: '))

if expression.count('(') == expression.count(')'):
    check = '\033[32mvalid\033[m'
else:
    check = '\033[31minvalid\033[m'

print(f'The expression is {check}')
