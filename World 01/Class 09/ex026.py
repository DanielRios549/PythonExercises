'''
    Get a phrase and show the following information:

    1 - How many times appears the letter 'A'
    2 - Which position it appears for the first time
    3 - Which position it appears for the last time
'''
sentence = input('Type a sentence: ').strip().lower()

print(f'''The letter A appears {sentence.count("a")} times in this sentence.
It appears for the first time at position {sentence.find("a") + 1},
It appears for the last time at position {sentence.rfind("a") + 1}.
''')
