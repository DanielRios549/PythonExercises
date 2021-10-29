'''
    Create a function called 'vote' that takes the year of birth as a parameter.
    The function should return the age of the person in that year.
    And show if the person should be able to vote or not.

    Return the options No, Optional or required.
'''


def vote(year: int):
    '''
        Verify if the person can vote or not.

        :param year: The year of birth.
    '''

    from datetime import date  # Local scope import

    today = date.today().year
    age = today - year

    if age < 16:
        type = '\033[31mcannot vote\033[m'
    elif (16 <= age < 18) or (age > 65):
        type = 'the vote is \033[34moptional\033[m'
    else:
        type = 'the vote is \033[32mrequired\033[m'

    print(f'For a person \033[34m{age}\033[m years old, {type}.')


vote(int(input('Enter your year of birth: ')))
