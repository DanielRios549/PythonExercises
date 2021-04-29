'''
    Get a phrase and show the following information:

    1 - How many times appears the letter 'A'
    2 - Which position it appears for the first time
    3 - Which position it appears for the last time
'''
sentence = input('Type a sentence: ').strip().lower()

print(f'''The letter A appears \033[34m{sentence.count("a")}\033[m times in this sentence.
It appears for the first time at position \033[32m{sentence.find("a") + 1}\033[m,
It appears for the last time at position \033[33m{sentence.rfind("a") + 1}\033[m.
''')
