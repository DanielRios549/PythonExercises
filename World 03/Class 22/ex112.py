'''
    Inside the utils package create in exercise 111, create a function called readMoney()
    that works like an input(), but contains a validation to accept only float values.
'''
import coin

number = coin.inputCoin('Choose a price: R$ ')

if type(number) is float:
    coin.summary(number, 10, 35)
