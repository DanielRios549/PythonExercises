'''
    Get a sentence and show if it is a palindrome
'''

sentence = ''.join(input('Type a sentence: ').strip().lower().split())
length = len(sentence)
inverse = sentence[::-1]

for count in range(0, (length // 2) + 1, 1):
    palindrome = True  # The sentence is a palindrome by default

    if sentence[count] != inverse[count]:  # But it verifies if really is, otherwise it is not and the loop is stopped
        palindrome = False
        break

if palindrome is True:
    print(f'This sentence \033[32mis\033[m a palindrome!')
else:
    print(f'This sentence \033[31mis not\033[m a palindrome!')
