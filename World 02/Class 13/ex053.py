'''
    Get a sentence and show if it is a palindrome
'''

sentence = ''.join(input('Type a sentence: ').strip().lower().split())
inverse = sentence[::-1]

if sentence == inverse:
    print(f'This sentence \033[32mis\033[m a palindrome!')
else:
    print(f'This sentence \033[31mis not\033[m a palindrome!')
