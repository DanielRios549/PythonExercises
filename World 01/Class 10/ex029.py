'''
    Get the speed of a car, if it was higher than 80Km/h, show a mesage saying they have a traffic ticket.
    The ticket will costs R$ 7,00 for each Km/h higher than the limit.
'''
speed = float(input('What is the speed of a car in Km/h? '))

if speed <= 80:
    print('Have a good day, sir!')
else:
    pay = (speed - 80) * 7
    print('Hey, you are too fast!')
    print(f'You will need to pay R$ {pay:.2f} for the traffic ticket.')
