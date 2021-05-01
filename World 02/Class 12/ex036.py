'''
    Approve a bank loan to buy a house. You need to get the house value, the buyer wage
    and how many years they will buy.

    Calculate the  mensal installment, knowing that it cannot exceed 30% of its wage,
    otherwise the loan will be rejected.
'''
house = float(input('How much the house costs? R$'))
salary = float(input('What is your salary? R$'))
years = int(input('How many years do you want to pay? '))

mensal = house / (years * 12)  # The payment will be monthly

if mensal > salary * 30 / 100:
    print('\033[31mREJECTED!!!\033[m')
    print(f'The installment of \033[34mR${mensal:.2f}\033[m is too high! \nIt would be \033[34m{mensal * 100 / salary:.2f}%\033[m of your salary.')
else:
    print('\033[32mACCEPTED!!!\033[m')
    print(f'You will pay \033[34mR${mensal:.2f}\033[m per month. \nThis is \033[34m{100 * mensal / salary:.2f}%\033[m of your salary')
