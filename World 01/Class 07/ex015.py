'''
    Create a program that asks how many kilometers a car racked up and the days it was rent for.
    Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per kilometer rack up.
'''

days = int(input('How many days you rent the car? '))
distance = float(input('How many kilometers the car racked up? '))
price = (60 * days) + (0.15 * distance)

print(f'You spend {days} days and the car racked up {distance}Km, the total price is R${price:.2f}.')
