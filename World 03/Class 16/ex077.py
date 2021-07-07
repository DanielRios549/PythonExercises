'''
    Create a tuple with some words. Show for each word its vowels.
'''

vowels = ('a', 'e', 'i', 'o', 'u')

words = (
    'Learn', 'Programming', 'Language', 'Python', 'Course', 'Free',
    'Study', 'Practice', 'Work', 'Market', 'Programmer', 'Future'
)

for word in words:
    print(f'\nThe word \033[34m{word}\033[m contains', end=' -> ')

    for letter in word:
        if letter in vowels:
            print(f'\033[32m{letter}\033[m', end=' ')
