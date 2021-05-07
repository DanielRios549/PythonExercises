'''
    Get the weight and the height of a person, show the BMI and show its status.

    Less than 18.5: Underweight
    Between 18.5 and 25: Normal weight
    Between 25 and 30: Overweight
    Between 30 and 40: Obesity
    More than 40: Morbid Obesity
'''
height = float(input('How tall is you? '))
weight = float(input('What\'s is your weight? '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = '\033[33mUnderweight\033[m'
elif bmi < 25:
    status = '\033[32mNormal weight\033[m'
elif bmi < 30:
    status = '\033[33mOverweight\033[m'
elif bmi <= 40:
    status = '\033[31mObesity\033[m'
else:
    status = '\033[31mMorbid Obesity\033[m'

print(f'A person \033[34m{height}m\033[m tall with \033[34m{weight}Kg\033[m has a BMI of \033[34m{bmi:.2f}\033[m and is {status}')
