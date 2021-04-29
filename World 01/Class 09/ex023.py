'''
    Get a number from 0 to 9999 and show all the digits separately
'''
number = int(input('input a number: '))

print(f'''Unit: \033[31m{number // 1 % 10}\033[m
Ten: \033[32m{number // 10 % 10}\033[m
Hundred: \033[33m{number // 100 % 10}\033[m
Thousand: \033[34m{number // 1000 % 10}\033[m
''')
