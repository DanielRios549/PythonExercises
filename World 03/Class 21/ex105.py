'''
    Create a function that takes the grades of students in a class
    and return a dictionary with the following data:

    1 - The numbers of grade
    2 - The highest grade
    3 - The lowest grade
    4 - The average of the class
    5 - The optional situation (good or bad)
'''


def notes(*notes, sit=False):
    '''
        Calculate a ramdom numbers of grades and show the situation.

        :param notes: One or more grades, you can pass various.
        :param sit: Show the situation, it is necessary to pass parameter name.
        :return: A dictionary with all the data.
    '''
    data = {
        'total': len(notes),
        'highest': max(notes),
        'lowest': min(notes),
        'average': sum(notes) / len(notes)
    }

    if sit is True:
        if data['average'] < 5:
            data['situation'] = 'BAD'

        elif 5 <= data['average'] <= 7:
            data['situation'] = 'OK'

        else:
            data['situation'] = 'Excellent'

    return data


student = notes(5.5, 2.5, 8.5, sit=True)
print(student)
