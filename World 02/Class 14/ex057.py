'''
    Get the gender of a person but only accept 'M' or 'F'.
    Otherwise, ask again until the user type the an acceptable value
'''

gender = input('What is you gender: [M/F] ').strip().upper()

while gender != 'M' and gender != 'F':
    print('Value not acceptable, choose M or F, please.')
    gender = input('What is your gender? ').strip().upper()
