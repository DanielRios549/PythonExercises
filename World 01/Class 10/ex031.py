'''
    Get the distance of a trip in Km. Calculate the price of the ticket, knowing that each Km costs R$0.50 for trips until 200Km,
    and R$ 0.45 for the ones longer than that.
'''

distance = float(input('What is the distance of the trip '))
print(f'You are near to start a trip of {distance:.1f}km')

price = 0.50 if distance <= 200 else 0.45
print(f'The trip will costs \033[34mR${distance * price:.2f}\033[m')
